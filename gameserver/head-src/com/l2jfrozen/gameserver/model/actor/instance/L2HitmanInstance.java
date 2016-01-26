/*
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation, either version 3 of the License, or (at your option) any later
 * version.
 * 
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 * 
 * You should have received a copy of the GNU General Public License along with
 * this program. If not, see <http://www.gnu.org/licenses/>.
 */
package com.l2jfrozen.gameserver.model.actor.instance;

import java.util.StringTokenizer;

import javolution.text.TextBuilder;
import javolution.util.FastList;

import com.l2jfrozen.gameserver.datatables.csv.MapRegionTable;
import com.l2jfrozen.gameserver.model.L2World;
import com.l2jfrozen.gameserver.model.actor.instance.L2NpcInstance;
import com.l2jfrozen.gameserver.model.entity.Hitman;
import com.l2jfrozen.gameserver.model.entity.PlayerToAssasinate;
import com.l2jfrozen.gameserver.network.serverpackets.NpcHtmlMessage;
import com.l2jfrozen.gameserver.templates.L2NpcTemplate;

/**
 * @author Setekh
 */
public class L2HitmanInstance extends L2NpcInstance
{
	public L2HitmanInstance(int objectID, L2NpcTemplate template)
	{
		super(objectID, template);
	}

	@Override
	public void onBypassFeedback(L2PcInstance player, String command)
	{
		StringTokenizer st = new StringTokenizer(command, " ");
		String currentcommand = st.nextToken();
		
		try
		{
			if(currentcommand.startsWith("showList"))
				parseWindow(player, showListWindow());
			else if(currentcommand.startsWith("showInfo"))
			{
				int playerId = Integer.parseInt(st.nextToken());
				parseWindow(player, showInfoWindow(playerId));
			}
			else if(currentcommand.startsWith("addList"))
			{
				String name = st.nextToken();
				int bounty = Integer.parseInt(st.nextToken());
				Hitman.getInstance().putHitOn(player, name, bounty);
			}
			else if(currentcommand.startsWith("removeList"))
			{
				String name = st.nextToken();
				Hitman.getInstance().cancelAssasination(name, player);
				showChatWindow(player, 0);
			}
			else
				super.onBypassFeedback(player, command);
		}
		catch (Exception e)
		{
			player.sendMessage("Action failed!");
			player.sendMessage("Make sure you filled the fields correctly.");
		}
	}
	
	public void parseWindow(L2PcInstance player, NpcHtmlMessage html)
	{
		html.replace("%objectId%", String.valueOf(getObjectId()));
		html.replace("%npc_name%", getName());
		html.replace("%player_name%", player.getName());
		html.replace("Setekh", "<font color=LEVEL>Setekh</font>");
		player.sendPacket(html);
	}
	
	public NpcHtmlMessage showListWindow()
	{
		TextBuilder content = new TextBuilder("<html><head><body><center>");
		NpcHtmlMessage html = new NpcHtmlMessage(getObjectId());
		
		content.append("<img src=L2Font-e.mini_logo-e width=245 height=80>");
		content.append("<img src=L2UI_CH3.herotower_deco width=256 height=32>");
		content.append("<font color=AAAAAA>Agency - Jobs</font><br>");
		content.append("<table height=10 bgcolor=0x0000CC border=1>");
		content.append("<tr><td width=100 align=center>Target</td>)");
		content.append("<td width=100 align=center>Bounty</td>");
		content.append("<td width=100 align=center>State</td></tr></table>");

		FastList<PlayerToAssasinate> list = new FastList<PlayerToAssasinate>();

		// First we parse the list.. so we woun't show just an empty list ^^
		for(PlayerToAssasinate pta : Hitman.getInstance().getTargets().values())
		{
			if(pta.isOnline() && !pta.isPendingDelete())
				list.add(pta);
		}
		
		// If the list contains at least 1 target we gonna make a html for him
		if(list.size() > 0)
		{
			for(PlayerToAssasinate pta: list)
			{
				content.append("<table height=10 bgcolor=FFFFFF border=1>");
				content.append("<tr><td width=100 align=center><button value=\"Infomation\" action=\"bypass -h npc_%objectId%_showInfo "+ pta.getObjectId() +"\" back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\" width=88 height=10></td>");
				content.append("<td width=100 align=center>" + pta.getBounty() + "</td>");
				content.append("<td width=100 align=center><font color=00FF00>Online</font></td></tr>");
				content.append("</table>");
			}
		}
		else // if not, we will add a message to our list: "No target is currently online."
		{
			content.append("<table height=10 bgcolor=FFFFFF border=1>");
			content.append("<tr><td width=50 align=center>&nbsp;</td>");
			content.append("<td width=200 align=center>No target is currently online.</td>");
			content.append("<td width=50 align=center>&nbsp;</td></tr>");
			content.append("</table>");
		}
		
		content.append("<br><font color=\"cc9900\"><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32></font><br1>");
		content.append("<img src=l2ui.bbs_lineage2 height=16 width=80>");
		content.append("<font color=AAAAAA>Gaming is not a crime. By Setekh</font>");
		content.append("</center></body></head></html>");
		html.setHtml(content.toString());
		
		return html;
	}

	public NpcHtmlMessage showInfoWindow(int objectId)
	{
		TextBuilder content = new TextBuilder("<html><head><body><center>");
		NpcHtmlMessage html = new NpcHtmlMessage(getObjectId());
		PlayerToAssasinate pta = Hitman.getInstance().getTargets().get(objectId);
		L2PcInstance target = L2World.getInstance().getPlayer(pta.getName());
		MapRegionTable map = MapRegionTable.getInstance();
		
		content.append("<img src=L2Font-e.mini_logo-e width=245 height=80>");
		content.append("<img src=L2UI_CH3.herotower_deco width=256 height=32>");
		content.append("<font color=AAAAAA>Target: "+pta.getName()+"</font><br>");
		content.append("</center><br>");
		
		if(target != null)
		{
			content.append("We are sorry %player_name% if we didn't manage to get more precise information.<br1> But you will have to do with this.<br>");
			content.append("<center><table border=1>");
			content.append("<tr><td width=250 align=left>");
			content.append("Name: "+pta.getName()+" <br1>");
			content.append("Bounty: "+pta.getBounty()+" Adena<br1>");
			content.append("Last Town: "+target.getLastTownName()+"<br1>");
			content.append("Current Known Location: "+map.getClosestTownName(target)+" Teritory");
			content.append("</td>");
			content.append("</tr>");
			content.append("</table>");
			content.append("</center><br>");
		}
		else
			content.append("Player went offline.");
		
		content.append("<center>");
		content.append("<button value=\"Back\" action=\"bypass -h npc_%objectId%_showList\" back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\" width=100 height=21>");
		content.append("<font color=\"cc9900\"><img src=\"L2UI_CH3.herotower_deco\" width=256 height=32></font><br1>");
		content.append("<img src=l2ui.bbs_lineage2 height=16 width=80>");
		content.append("<font color=AAAAAA>Gaming is not a crime. By Setekh</font>");
		content.append("</center></body></head></html>");
		html.setHtml(content.toString());

		return html;
	}
}