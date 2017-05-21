/* This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
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

import java.security.MessageDigest;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.StringTokenizer;

import com.l2jfrozen.Config;
import com.l2jfrozen.crypt.Base64;
import com.l2jfrozen.gameserver.ai.CtrlIntention;
import com.l2jfrozen.gameserver.network.serverpackets.ActionFailed;
import com.l2jfrozen.gameserver.network.serverpackets.LeaveWorld;
import com.l2jfrozen.gameserver.network.serverpackets.MyTargetSelected;
import com.l2jfrozen.gameserver.network.serverpackets.NpcHtmlMessage;
import com.l2jfrozen.gameserver.network.serverpackets.ValidateLocation;
import com.l2jfrozen.gameserver.templates.L2NpcTemplate;
import com.l2jfrozen.util.CloseUtil;
import com.l2jfrozen.util.database.L2DatabaseFactory;

public class L2ChangePasswordInstance extends L2FolkInstance
{
 public L2ChangePasswordInstance(int objectId, L2NpcTemplate template)
 {
 super(objectId, template);
 }

 @Override
 public void onAction(L2PcInstance player)
 {
 if (!canTarget(player))
 {
 return;
 }

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
 showHtmlWindow(player);
 }
 }

 player.sendPacket(new ActionFailed());
 }

 private void showHtmlWindow(L2PcInstance player)
 {
 String filename = "data/html/mods/change_password.htm";
 NpcHtmlMessage html = new NpcHtmlMessage(1);
 html.setFile(filename);
 html.replace("%objectId%", String.valueOf(getObjectId()));
 player.sendPacket(html);
 filename = null;
 html = null;
 }

 @Override
 public void onBypassFeedback(L2PcInstance player, String command)
 {
 if (command.startsWith("change_password"))
 {
 StringTokenizer st = new StringTokenizer(command);
 st.nextToken();
 String curPass = null;
 String newPass = null;
 String repPass = null;
 try
 {
 if (st.hasMoreTokens())
 {
 curPass = st.nextToken();
 newPass = st.nextToken();
 repPass = st.nextToken();
 }
 else
 {
 player.sendMessage("Please fill in all the blanks before requesting for a password change.");
 return;
 }
 changePassword(curPass, newPass, repPass, player);
 }
 catch (StringIndexOutOfBoundsException e)
 {
 if (Config.ENABLE_ALL_EXCEPTIONS)
 {
 e.printStackTrace();
 }
 }
 }
 }

 public static boolean changePassword(String currPass, String newPass, String repeatNewPass, L2PcInstance activeChar)
 {
 if (newPass.length() < 3)
 {
 activeChar.sendMessage("Nova senha muito curta!");
 return false;
 }
 if (newPass.length() > 16)
 {
 activeChar.sendMessage("Nova senha muito longa!");
 return false;
 }
 if (!newPass.equals(repeatNewPass))
 {
 activeChar.sendMessage("Campos de Nova senha nao estao iguais!");
 return false;
 }

 Connection con = null;
 String password = null;
 try
 {
 MessageDigest md = MessageDigest.getInstance("SHA");
 byte[] raw = currPass.getBytes("UTF-8");
 raw = md.digest(raw);
 String currPassEncoded = Base64.encodeBytes(raw);

 con = L2DatabaseFactory.getInstance().getConnection(false);
 PreparedStatement statement = con.prepareStatement("SELECT password FROM accounts WHERE login=?");
 statement.setString(1, activeChar.getAccountName());
 ResultSet rset = statement.executeQuery();
 while (rset.next())
 {
 password = rset.getString("password");
 }
 rset.close();
 statement.close();
 byte[] password2 = null;
 if (currPassEncoded.equals(password))
 {
 password2 = newPass.getBytes("UTF-8");
 password2 = md.digest(password2);

 PreparedStatement statement2 = con.prepareStatement("UPDATE accounts SET password=? WHERE login=?");
 statement2.setString(1, Base64.encodeBytes(password2));
 statement2.setString(2, activeChar.getAccountName());
 statement2.executeUpdate();
 statement2.close();

 activeChar.sendMessage("Sua senha foi alterada! Por seguranca, Voce sera desconectado. Por favor, faca login novamente!");
 try
 {
 Thread.sleep(3000L);
 }
 catch (Exception e)
 {
 if (Config.ENABLE_ALL_EXCEPTIONS)
 {
 e.printStackTrace();
 }
 }

 activeChar.deleteMe();
 activeChar.sendPacket(new LeaveWorld());
 }
 else
 {
 activeChar.sendMessage("Senha atual Incorreta! Por favor, tente novamente!");

 return password2 != null;
 }
 }
 catch (Exception e)
 {
 if (Config.ENABLE_ALL_EXCEPTIONS)
 {
 e.printStackTrace();
 }

 _log.warning("could not update the password of account: " + activeChar.getAccountName());
 }
 finally
 {
 CloseUtil.close(con);
 }

 return true;
 }
}