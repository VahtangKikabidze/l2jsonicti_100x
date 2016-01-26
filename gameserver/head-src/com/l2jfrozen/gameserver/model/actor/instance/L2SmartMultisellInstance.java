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

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.StringTokenizer;

import com.l2jfrozen.gameserver.ai.CtrlIntention;
import com.l2jfrozen.gameserver.datatables.sql.ItemTable;
import com.l2jfrozen.gameserver.network.SystemMessageId;
import com.l2jfrozen.gameserver.network.serverpackets.ActionFailed;
import com.l2jfrozen.gameserver.network.serverpackets.CharInfo;
import com.l2jfrozen.gameserver.network.serverpackets.InventoryUpdate;
import com.l2jfrozen.gameserver.network.serverpackets.MyTargetSelected;
import com.l2jfrozen.gameserver.network.serverpackets.NpcHtmlMessage;
import com.l2jfrozen.gameserver.network.serverpackets.SystemMessage;
import com.l2jfrozen.gameserver.network.serverpackets.UserInfo;
import com.l2jfrozen.gameserver.network.serverpackets.ValidateLocation;
import com.l2jfrozen.gameserver.model.actor.instance.L2PcInstance;
import com.l2jfrozen.gameserver.templates.L2NpcTemplate;
import com.l2jfrozen.util.CloseUtil;
import com.l2jfrozen.util.database.L2DatabaseFactory;

import javolution.text.TextBuilder;

/**
 * 
 * @author Elfocrash
 *
 */

public class L2SmartMultisellInstance extends L2FolkInstance
{
  public L2SmartMultisellInstance(int objectId, L2NpcTemplate template)
  {
    super(objectId, template);
  }

  @Override
public void onBypassFeedback(L2PcInstance player, String command)
  {
         if(player == null)
         {
            return;
         }

         if(command.startsWith("buyItem "))
         {
         String itemId = null;
         StringTokenizer st = new StringTokenizer(command, " ");
         
         while (st.hasMoreTokens())
         {
         itemId = st.nextToken();
         }
         
         int id = Integer.parseInt(itemId);
         
         if(player.getInventory().getItemByItemId(getItemCostId(id)).getCount() >= getItemCostCount(id))
         {
         player.getInventory().destroyItemByItemId("delete", getItemCostId(id), getItemCostCount(id), player, null);
         
   L2ItemInstance item = null;      
   item = player.getInventory().addItem("Elfo", getItemId(id), 1, null, null);
   item.setEnchantLevel(getItemEnchant(id));

// send packets
InventoryUpdate iu = new InventoryUpdate();
iu.addItem(item);
player.sendPacket(iu);
player.broadcastPacket(new CharInfo(player));
player.sendPacket(new UserInfo(player));

SystemMessage sm = new SystemMessage(SystemMessageId.YOU_PICKED_UP_S1_S2);
sm.addItemName(item.getItemId());
sm.addNumber(1);
player.sendPacket(sm);
iu = null;
         }
         else
         {
         player.sendMessage("Voce nao possui os Itens necessarios para comprar");
         return;
         }
         }

  }

  @Override
public void onAction(L2PcInstance player)
 {
   if (!canTarget(player)) {
     return;
   }

   if (this != player.getTarget())
   {
     player.setTarget(this);

     player.sendPacket(new MyTargetSelected(getObjectId(), 0));

     player.sendPacket(new ValidateLocation(this));
   }
   else if (!canInteract(player))
   {
     player.getAI().setIntention(CtrlIntention.AI_INTENTION_INTERACT, this);
   }
   else
   {
    showHtmlWindow(player);
   }

   player.sendPacket(new ActionFailed());
 }

  private void showHtmlWindow(L2PcInstance activeChar)
  {
    NpcHtmlMessage nhm = new NpcHtmlMessage(5);
    TextBuilder tb = new TextBuilder("");

    tb.append("<html><head><title>SonicTi Shop</title></head><body>");
    tb.append("<center>");
    tb.append("<table width=\"250\" cellpadding=\"5\" bgcolor=\"000000\">");
    tb.append("<tr>");
    tb.append("<td width=\"45\" valign=\"top\" align=\"center\"><img src=\"L2ui_ch3.menubutton4\" width=\"38\" height=\"38\"></td>");
    tb.append("<td valign=\"top\"><font color=\"FF6600\">Smart Shop</font>"); 
    tb.append("<br1><font color=\"00FF00\">"+activeChar.getName()+"</font>, deseja alguma coisa?</td>");
    tb.append("</tr>");
    tb.append("</table>");
    tb.append("</center>");
    tb.append("<center>");

    for(int i = 1; i<= getRowsCount(); i++)
     tb.append("<br><a action=\"bypass -h npc_" + getObjectId() + "_buyItem " + i + "\">Item: " + ItemTable.getInstance().getTemplate(getItemId(i)).getName() + " Enchant: +"+ getItemEnchant(i) + " Cost: " + getItemCostCount(i) + " " + ItemTable.getInstance().getTemplate(getItemCostId(i)).getName() + "</a>");

    tb.append("</center>");
    tb.append("<center>");
    tb.append("<img src=\"l2ui_ch3.herotower_deco\" width=256 height=32 align=center>");
    tb.append("<font color=\"FF6600\">SonicTi Shop</font>"); 
    tb.append("</center>");
    tb.append("</body></html>");

    nhm.setHtml(tb.toString());
    activeChar.sendPacket(nhm);

    activeChar.sendPacket(new ActionFailed());
  }

  private int getRowsCount()
  {
      int rows = 0;
      Connection con = null;
      try
      {
              con = L2DatabaseFactory.getInstance().getConnection();

              PreparedStatement statement = con.prepareStatement("SELECT * FROM smart_shop");

              ResultSet rset = statement.executeQuery();
              while (rset.next())
              {
                  rows++;
              }
   rset.close();
   statement.close();

      }
catch(Exception e)
{
e.printStackTrace();
}finally{
CloseUtil.close(con);
con = null;
}
      return rows;

  }

  private int getItemId(int itemId)
  {
      int itemIdd = 0;
      Connection con = null;
      try
      {
              con = L2DatabaseFactory.getInstance().getConnection();

              PreparedStatement statement = con.prepareStatement("SELECT item_id FROM smart_shop WHERE id=?");
              statement.setInt(1, itemId);

              ResultSet rset = statement.executeQuery();
              while (rset.next())
              {
               itemIdd = rset.getInt("item_id");
              }
     rset.close();
       statement.close();

      }
catch(Exception e)
{
e.printStackTrace();
}finally{
CloseUtil.close(con);
con = null;
}
      return itemIdd;

  }

  private int getItemCostId(int costid)
  {
      int costIt = 0;
      Connection con = null;
      try
      {
              con = L2DatabaseFactory.getInstance().getConnection();

              PreparedStatement statement = con.prepareStatement("SELECT cost_item_id FROM smart_shop WHERE id=?");
              statement.setInt(1, costid);

              ResultSet rset = statement.executeQuery();
              while (rset.next())
              {
               costIt = rset.getInt("cost_item_id");
              }
     rset.close();
       statement.close();

      }
catch(Exception e)
{
e.printStackTrace();
}finally{
CloseUtil.close(con);
con = null;
}
      return costIt;

  }

  private int getItemCostCount(int costid)
  {
      int costIt = 0;
      Connection con = null;
      try
      {
              con = L2DatabaseFactory.getInstance().getConnection();

              PreparedStatement statement = con.prepareStatement("SELECT cost_item_count FROM smart_shop WHERE id=?");
              statement.setInt(1, costid);

              ResultSet rset = statement.executeQuery();
              while (rset.next())
              {
               costIt = rset.getInt("cost_item_count");
              }
     rset.close();
       statement.close();

      }
catch(Exception e)
{
e.printStackTrace();
}finally{
CloseUtil.close(con);
con = null;
}
      return costIt;

  }

  private int getItemEnchant(int id)
  {
      int itemEnch = 0;
      Connection con = null;
      PreparedStatement statement = null;
      try
      {
              con = L2DatabaseFactory.getInstance().getConnection();

              statement = con.prepareStatement("SELECT item_enchant FROM smart_shop WHERE id=?");
              statement.setInt(1, id);

              ResultSet rset = statement.executeQuery();
              while (rset.next())
              {
               itemEnch = rset.getInt("item_enchant");
              }
     rset.close();
       statement.close();

      }
catch(Exception e)
{
e.printStackTrace();
}finally{
CloseUtil.close(con);
con = null;
}
      return itemEnch;

  }

}