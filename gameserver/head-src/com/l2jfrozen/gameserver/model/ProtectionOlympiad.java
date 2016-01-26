package com.l2jfrozen.gameserver.model;



import com.l2jfrozen.Config;
import com.l2jfrozen.gameserver.model.entity.Announcements;
import com.l2jfrozen.gameserver.thread.ThreadPoolManager;
import com.l2jfrozen.gameserver.network.clientpackets.Say2;
import com.l2jfrozen.gameserver.model.L2World;
import com.l2jfrozen.gameserver.model.actor.instance.L2PcInstance;
import com.l2jfrozen.gameserver.network.serverpackets.CreatureSay;


public class ProtectionOlympiad

{

public static void disc(final L2PcInstance player)

{

player.sendPacket(new CreatureSay(1, Say2.HERO_VOICE, "[Olympiad Anti Bot]", " "+ player.getName() +" check player bot status ..."));

ThreadPoolManager.getInstance().scheduleGeneral(new Runnable()

{

public void run()

{

// Kick Punish

if(Config.ENABLE_BOT_PUNISH){

player.closeNetConnection();

// Announce Kick

Announcements.getInstance().olympiadAnnounceToAll(" "+player.getName()+" just been kicked by anti bot olympiad!.");

// Ban Punish

player.setAccessLevel(Config.BAN_THIS_PLAYER_ACESSLEVEL);



}

}

}, 20000);

}

public static boolean check(L2PcInstance player)

{

boolean loggedz0r = false;

for (L2PcInstance playerz0r : L2World.getInstance().getAllPlayers())

{

String client = first(playerz0r);

String client1 = second(player);

if (client.equalsIgnoreCase(client1));

loggedz0r = true;

}

return loggedz0r;

}

private static String first(L2PcInstance player)

{

return second(player).toString();

}

private static String second(L2PcInstance player)

{

try

{

return player.getClient().getConnection().getInetAddress().getHostAddress();

} catch (Throwable t){}

return null;

}

}