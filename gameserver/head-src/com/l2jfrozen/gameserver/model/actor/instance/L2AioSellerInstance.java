/* This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
 * 02111-1307, USA.
 *
 * http://www.gnu.org/copyleft/gpl.html
 */
package com.l2jfrozen.gameserver.model.actor.instance;

import java.util.StringTokenizer;

import com.l2jfrozen.Config;
import com.l2jfrozen.gameserver.ai.CtrlIntention;
import com.l2jfrozen.gameserver.network.SystemMessageId;
import com.l2jfrozen.gameserver.network.serverpackets.ActionFailed;
import com.l2jfrozen.gameserver.network.serverpackets.EtcStatusUpdate;
import com.l2jfrozen.gameserver.network.serverpackets.InventoryUpdate;
import com.l2jfrozen.gameserver.network.serverpackets.MyTargetSelected;
import com.l2jfrozen.gameserver.network.serverpackets.NpcHtmlMessage;
import com.l2jfrozen.gameserver.network.serverpackets.SystemMessage;
import com.l2jfrozen.gameserver.network.serverpackets.ValidateLocation;
import com.l2jfrozen.gameserver.templates.L2NpcTemplate;

/**
 * Aio Shop e um re-make do Mod Aio Seller. De uma versao para outra, muitas coisas mudaram e isto altera o modo de usar do mod por completo!
 * Agora e possivel alterar a template, o item, o preco e o tempo via html. Em resumo, esta nova versao do codigo esta bem mais flexivel.
 * Faca um bom uso! 
 * @author RedHoT
 * @version 1.0.7
 */
public class L2AioSellerInstance extends L2FolkInstance
{
	public L2AioSellerInstance(int objectId, L2NpcTemplate template)
	{
		super(objectId, template);
	}

	@Override
	public void onAction(L2PcInstance player)
	{
		if (!canTarget(player))
			return;

		player.setLastFolkNPC(this);

		// Check if the L2PcInstance already target the L2NpcInstance
		if (this != player.getTarget())
		{
			// Set the target of the L2PcInstance player
			player.setTarget(this);

			// Send a Server->Client packet MyTargetSelected to the L2PcInstance player
			MyTargetSelected my = new MyTargetSelected(getObjectId(), 0);
			player.sendPacket(my);
			my = null;

			// Send a Server->Client packet ValidateLocation to correct the L2NpcInstance position and heading on the client
			player.sendPacket(new ValidateLocation(this));
		}
		else
		{
			// Calculate the distance between the L2PcInstance and the L2NpcInstance
			if (!canInteract(player))
			{
				// Notify the L2PcInstance AI with AI_INTENTION_INTERACT
				player.getAI().setIntention(CtrlIntention.AI_INTENTION_INTERACT, this);
			}
			else
			{
				showMessageWindow(player);
			}
		}
		// Send a Server->Client ActionFailed to the L2PcInstance in order to avoid that the client wait another packet
		player.sendPacket(ActionFailed.STATIC_PACKET);
	}

	private void showMessageWindow(L2PcInstance player)
	{
		String filename = "data/html/mods/Aio Shop/start.htm";

		NpcHtmlMessage html = new NpcHtmlMessage(1);
		html.setFile(filename);
		html.replace("%objectId%", String.valueOf(getObjectId()));
		html.replace("%servername%", Config.ALT_Server_Name);
		player.sendPacket(html);
		filename = null;
		html = null;
	}

	@Override
	public void onBypassFeedback(L2PcInstance player, String command)
	{
		if (command.startsWith("add_aio"))
		{
			StringTokenizer st = new StringTokenizer(command);
			st.nextToken();

			String priceId = null, priceCount = null, time = null;
			int aioPriceId = 0, aioPriceCount = 0, aioTime = 0; 

			if (st.hasMoreTokens())
			{
				priceId = st.nextToken();
				priceCount = st.nextToken();
				time = st.nextToken();

				try
				{
					aioPriceId = Integer.parseInt(priceId);
					aioPriceCount = Integer.parseInt(priceCount);
					aioTime = Integer.parseInt(time);
				}
				catch(NumberFormatException e) {}
			}
			else
			{
				_log.warning("Could not update aio status of player " + player.getName());
				return;
			}

			makeAioCharacter(player, aioPriceId, aioPriceCount, aioTime);
		}
		else if (command.startsWith("remove_aio"))
			removeAio(player);

		showMessageWindow(player);
	}

	
	public void makeAioCharacter(L2PcInstance player, int itemId, int itemCount, int aioTime)
	{
		L2ItemInstance itemInstance = player.getInventory().getItemByItemId(itemId);

		if (itemInstance == null || !itemInstance.isStackable() && player.getInventory().getInventoryItemCount(itemId, -1) < (itemCount))
		{
            player.sendPacket(new SystemMessage(SystemMessageId.NOT_ENOUGH_ITEMS));
			return;
		}
		else if (itemInstance.isStackable())
		{
			if (!player.destroyItemByItemId("Aio", itemId, itemCount, player.getTarget(), true))
			{
                player.sendPacket(new SystemMessage(SystemMessageId.NOT_ENOUGH_ITEMS));
				return;
			}
		}
		else
			for (int i = 0; i < (itemCount); i++)
				player.destroyItemByItemId("Aio", itemId, 1, player.getTarget(), true);

		doAio(player, aioTime);
	}
	public void doAio(L2PcInstance player, int days)
	{
		if(player == null)
			return;

        int daysLeft = player.getAioEndTime() <= 0 ? 0 : (int) ((player.getAioEndTime() - System.currentTimeMillis()) / 86400000);
		player.setAio(true);
		player.setEndTime("aio", days + daysLeft);

		player.getStat().addExp(player.getStat().getExpForLevel(81));

		if(Config.ALLOW_AIO_NCOLOR && player.isAio())
			player.getAppearance().setNameColor(Config.AIO_NCOLOR);

		if(Config.ALLOW_AIO_TCOLOR && player.isAio())
			player.getAppearance().setTitleColor(Config.AIO_TCOLOR);

		/* Give Aio Dual */
		L2ItemInstance item;
		if(player.getInventory().getItemByItemId(Config.DUAL_AIO_ID) == null)
		{
			item = player.getInventory().addItem("", Config.DUAL_AIO_ID, 1, player, null);
			InventoryUpdate iu = new InventoryUpdate();
			iu.addItem(item);
			player.sendPacket(iu);
		}

		player.rewardAioSkills();
		player.sendPacket(new EtcStatusUpdate(player));
		player.sendSkillList();
		player.broadcastUserInfo();

		player.sendMessage("You are now an Aio, Congratulations!");
	}

	public void removeAio(L2PcInstance player)
	{
		if(!player.isAio())
		{
			player.sendMessage("You are not an AIO.");
			return;
		}

		player.setAio(false);
		player.setAioEndTime(0);

		player.getAppearance().setNameColor(0xFFFFFF);
		player.getAppearance().setTitleColor(0xFFFF77);

		/* Remove Aio Dual */
		L2ItemInstance item;
		player.getWarehouse().destroyItemByItemId("", Config.DUAL_AIO_ID, 1, player, null);
		item = player.getInventory().destroyItemByItemId("", Config.DUAL_AIO_ID, 1, player, null);
		InventoryUpdate iu = new InventoryUpdate();
		iu.addItem(item);
		player.sendPacket(iu);
   			
		player.lostAioSkills();
		player.sendPacket(new EtcStatusUpdate(player));
		player.sendSkillList();
		player.broadcastUserInfo();

		player.sendMessage("Now You are not an Aio..");
	}
}