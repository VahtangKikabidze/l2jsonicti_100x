import sys
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from java.util import Iterator
from com.l2jfrozen.gameserver.datatables import SkillTable
from com.l2jfrozen.util.database import L2DatabaseFactory
from com.l2jfrozen.gameserver.model.actor.appearance import PcAppearance
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.actor.appearance import PcAppearance
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest


NPC=[1006]
ADENA_ID = 57

QuestId     = 88555
QuestName   = "Rankings"
QuestDesc   = "custom"
InitialHtml = "1.htm"

class Quest (JQuest) :

	def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)


	def onTalk (self,npc,player):
		return InitialHtml



	def onEvent(self,event,st):
		htmltext = event
		count = st.getQuestItemsCount(ADENA_ID)
		
		if event == "1" and count >= 10000 :
			st.takeItems(ADENA_ID,10000)
			htmltext_ini = "<html><head><title>PK Information</title></head><body><table width=290><tr><td><center>Rank</center></td><td><center>Character</center></td><td><center>Class</center></td><td><center>Kills</center></td></tr>"
			htmltext_info =""			
			color = 1
			pos = 0
			con = L2DatabaseFactory.getInstance().getConnection()
			pk = con.prepareStatement("SELECT char_name,classid,pkkills FROM characters WHERE pkkills>0 and accesslevel=0 order by pkkills desc limit 30")
			rs = pk.executeQuery()
			while (rs.next()) :
				char_name = rs.getString("char_name")
                                char_class = rs.getString("classid")
				char_pkkills = rs.getString("pkkills")
				pos = pos + 1
				posstr = str(pos)
				classname = con.prepareStatement("SELECT classname FROM char_templates WHERE classid=" + char_class)
				rs2 = classname.executeQuery()
				while (rs2.next()) :
					char_zeor = rs2.getString("classname")
				if color == 1:
					color_text = "<font color =\"effe00\">"
					color = 2
					htmltext_info = htmltext_info + "<tr><td><center><font color =\"effe00\">" + posstr + "</td><td><center>" + color_text + char_name +"</center></td><td><center>" + color_text + char_zeor +"</center></td><td><center>" + char_pkkills + "</center></td></tr>"
				elif color == 2:
					color_text = "<font color =\"06db33\">"
					color = 1
					htmltext_info = htmltext_info + "<tr><td><center><font color =\"06db33\">" + posstr + "</td><td><center>" + color_text + char_name +"</center></td><td><center>" + color_text + char_zeor +"</center></td><td><center>" + char_pkkills + "</center></td></tr>"
			htmltext_pklist = htmltext_ini + htmltext_info
			con.close()
			return htmltext_pklist
		elif event == "1" and count < 10000 :
			htmltext = "<html><head><title>PK Information</title></head><body><font color =\"FF0000\">You don't have enought adena.</body></html>"
			return htmltext
			
			
		if event == "2" and count >= 10000 :
			st.takeItems(ADENA_ID,10000)
			htmltext_ini = "<html><head><title>PvP Information</title></head><body><table width=290><tr><td><center>Rank</center></td><td><center>Character</center></td><td><center>Class</center></td><td><center>Kills</center></td></tr>"
			htmltext_info =""			
			color = 1
			pos = 0
			con = L2DatabaseFactory.getInstance().getConnection()
			pvp = con.prepareStatement("SELECT char_name,classid,pvpkills FROM characters WHERE pvpkills>0 and accesslevel=0 order by pvpkills desc limit 30")
			rs = pvp.executeQuery()
			while (rs.next()) :
				char_name = rs.getString("char_name")
                                char_class = rs.getString("classid")
				char_pvpkills = rs.getString("pvpkills")
				pos = pos + 1
				posstr = str(pos)
				classname = con.prepareStatement("SELECT classname FROM char_templates WHERE classid=" + char_class)
				rs2 = classname.executeQuery()
				while (rs2.next()) :
					char_zeor = rs2.getString("classname")
				if color == 1:
					color_text = "<font color =\"effe00\">"
					color = 2
					htmltext_info = htmltext_info + "<tr><td><center><font color =\"effe00\">" + posstr + "</center></td><td><center>" + color_text + char_name +"</center></td><td><center>" + color_text + char_zeor +"</center></td><td><center>" + char_pvpkills + "</center></td></tr>"
				elif color == 2:
					color_text = "<font color =\"06db33\">"
					color = 1
					htmltext_info = htmltext_info + "<tr><td><center><font color =\"06db33\">" + posstr + "</center></td><td><center>" + color_text + char_name +"</center></td><td><center>" + color_text + char_zeor +"</center></td><td><center>" + char_pvpkills + "</center></td></tr>"
			htmltext_pklist = htmltext_ini + htmltext_info
			con.close()
			return htmltext_pklist
		elif event == "2" and count < 10000 :
			htmltext = "<html><head><title>PvP Information</title></head><body><font color =\"FF0000\">You don't have enought adena.</body></html>"
			return htmltext


		if event == "3" and count >= 10000 :
			st.takeItems(ADENA_ID,10000)
			htmltext_ini = "<html><head><title>Clan Information</title></head><body><table width=290><tr><td><center>Rank</center></td><td><center>Level</center></td><td><center>Clan Name</center></td><td><center>Reputation</center></td></tr>"
			htmltext_info =""
			color = 1
			pos = 0
			con = L2DatabaseFactory.getInstance().getConnection()
			clan = con.prepareStatement("SELECT clan_name,clan_level,reputation_score FROM clan_data WHERE clan_level>0 order by reputation_score desc limit 15")
			rs = clan.executeQuery()
			while (rs.next()) :
				clan_name = rs.getString("clan_name")
				clan_level = rs.getString("clan_level")
				clan_score = rs.getString("reputation_score")
				pos = pos + 1
				posstr = str(pos)
				if color == 1:
					color_text = "<font color =\"effe00\">"
					color = 2
					htmltext_info = htmltext_info + "<tr><td><center><font color =\"effe00\">" + posstr + "</center></td><td><center>" + color_text + clan_level +"</center></td><td><center>" + clan_name + "</center></td><td><center>" + clan_score + "</center></td></tr>"
				elif color == 2:
					color_text = "<font color =\"06db33\">"
					color = 1
					htmltext_info = htmltext_info + "<tr><td><center><font color =\"06db33\">" + posstr + "</center></td><td><center>" + color_text + clan_level +"</center></td><td><center>" + clan_name + "</center></td><td><center>" + clan_score + "</center></td></tr>"
			htmltext_pklist = htmltext_ini + htmltext_info
			con.close()
			return htmltext_pklist
		elif event == "3" and count < 10000 :
			htmltext = "<html><head><title>Clan Information</title></head><body><font color =\"FF0000\">You don't have enought adena.</body></html>"
			return htmltext


QUEST       = Quest(QuestId,str(QuestId) + "_" + QuestName,QuestDesc)
CREATED=State('Start',QUEST)
STARTED=State('Started',QUEST)
COMPLETED=State('Completed',QUEST)

QUEST.setInitialState(CREATED)

for npcId in NPC:
 QUEST.addStartNpc(npcId)
 QUEST.addTalkId(npcId)