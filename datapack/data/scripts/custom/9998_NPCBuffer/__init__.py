import sys
from com.l2jfrozen.gameserver.model.actor.instance import L2PcInstance
from java.util import Iterator
from com.l2jfrozen.gameserver.datatables import SkillTable
from com.l2jfrozen.util.database import L2DatabaseFactory
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "9999_NPCBuffer"

NPC=[9998]
ADENA_ID=57
QuestId     = 9999
QuestName   = "NPCBuffer"
QuestDesc   = "custom"
InitialHtml = "1.htm"

print "importing custom: 9999: NPCBuffer"

class Quest (JQuest) :

	def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)


	def onEvent(self,event,st):
		htmltext = event
		count=st.getQuestItemsCount(ADENA_ID)
		if count < 0  or st.getPlayer().getLevel() < 1 :
			htmltext = "<html><head><body>You dont have enough Adena,<br> or your level is too low. You must be 40 or higher.</body></html>"
		else:
			st.takeItems(ADENA_ID,0)
			st.getPlayer().setTarget(st.getPlayer())
			
			#Wind Walk
			if event == "2":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1204,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Decrease Weight
			if event == "3":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1257,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Shield
			if event == "4":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1040,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Might
			if event == "5":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1068,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Mental Shield
			if event == "6":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1035,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless the Body
			if event == "7":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1045,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless the Soul
			if event == "8":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1048,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Magic Barrier
			if event == "9":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1036,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Concentration
			if event == "10":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1078,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Berserker Spirit
			if event == "11":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1062,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Bless Shield
			if event == "12":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1243,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Vampiric Rage
			if event == "13":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1268,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Acumen
			if event == "14":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1085,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Empower
			if event == "15":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1059,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Haste
			if event == "16":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1086,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Guidance
			if event == "17":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1240,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Focus
			if event == "18":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1077,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Death Whisper
			if event == "19":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1242,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

                        #Agility
			if event == "20":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1087,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"
				st.setState(COMPLETED)	
                                                
                        #Clarity
			if event == "21":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1397,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"
				st.setState(COMPLETED)	
                                                
                        #Advanced Block
			if event == "22":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1304,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"
				st.setState(COMPLETED)	
                                                
                        #Kiss of Eva
			if event == "23":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1073,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"
				st.setState(COMPLETED)	
                                                
                        #Greater Shield
			if event == "24":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1389,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"
				st.setState(COMPLETED)	
                                               
                        #Wild Magic
			if event == "25":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1303,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"
				st.setState(COMPLETED)

			#Regeneration
			if event == "26":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1044,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Holy Weapon
			if event == "27":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1043,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Mana Regeneration
			if event == "28":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1047,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Greather Might
			if event == "29":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1388,1).getEffects(st.getPlayer(),st.getPlayer())
				return "2.htm"		
				st.setState(COMPLETED)

			#Chant of battle
			if event == "30":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1007,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Shielding
			if event == "31":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1009,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Fire
			if event == "32":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1006,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Flame
			if event == "33":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1002,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Fury
			if event == "34":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1251,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Evasion
			if event == "35":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1252,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Rage
			if event == "36":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1253,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Revenge
			if event == "37":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1284,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Vampire
			if event == "38":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1310,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Eagle
			if event == "39":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1309,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Predator
			if event == "40":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1308,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Spirit
			if event == "41":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1362,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Victory
			if event == "42":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1363,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of Magnus
			if event == "43":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1413,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#War Chant
			if event == "44":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1390,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Earth Chant
			if event == "45":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1391,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Chant of life
			if event == "46":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1229,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Body Avatar
			if event == "47":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1311,1).getEffects(st.getPlayer(),st.getPlayer())
				return "3.htm"		
				st.setState(COMPLETED)

			#Profecy of Fire
			if event == "48":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1356,1).getEffects(st.getPlayer(),st.getPlayer())
				return "4.htm"		
				st.setState(COMPLETED)

			#Profecy of Wather
			if event == "49":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1355,1).getEffects(st.getPlayer(),st.getPlayer())
				return "4.htm"		
				st.setState(COMPLETED)

			#profecy of Wind
			if event == "50":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1357,1).getEffects(st.getPlayer(),st.getPlayer())
				return "4.htm"		
				st.setState(COMPLETED)

			#Blessing of Queen
			if event == "51":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(4699,1).getEffects(st.getPlayer(),st.getPlayer())
				return "5.htm"		
				st.setState(COMPLETED)

			#Blessing of Seraphim
			if event == "52":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(4702,1).getEffects(st.getPlayer(),st.getPlayer())
				return "5.htm"		
				st.setState(COMPLETED)

			#Gifth Queen
			if event == "53":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(4703,1).getEffects(st.getPlayer(),st.getPlayer())
				return "5.htm"		
				st.setState(COMPLETED)

			#Gifth Seraphim
			if event == "54":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(4700,1).getEffects(st.getPlayer(),st.getPlayer())
				return "5.htm"		
				st.setState(COMPLETED)

			#Holy Resistance
			if event == "55":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1392,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Unholy Resistance
			if event == "56":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1393,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Resist Aqua
			if event == "57":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1182,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Resist Wind
			if event == "58":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1189,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Resist Fire
			if event == "59":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1191,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Resist Poison
			if event == "60":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1033,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Elemetal Protection
			if event == "61":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1352,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Arcane Protection
			if event == "62":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1354,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Divine Protection
			if event == "63":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1353,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Invigor
			if event == "64":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1032,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Resist Shock
			if event == "65":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1259,1).getEffects(st.getPlayer(),st.getPlayer())
				return "6.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Gifth
			if event == "66":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1003,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Blessing
			if event == "67":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1005,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Glory
			if event == "68":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1008,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Tact
			if event == "69":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1260,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Wisdom
			if event == "70":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1004,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Protection
			if event == "71":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1250,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Rage
			if event == "72":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1261,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Vision
			if event == "73":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1249,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Haste
			if event == "74":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1282,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Eye
			if event == "75":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1364,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Soul
			if event == "76":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1365,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Emblem
			if event == "77":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1415,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Fist
			if event == "78":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1416,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Pa'agrio Victory
			if event == "79":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1414,1).getEffects(st.getPlayer(),st.getPlayer())
				return "7.htm"		
				st.setState(COMPLETED)

			#Dance of Warrior
			if event == "80":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(271,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Inspiration
			if event == "81":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(272,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Mystic
			if event == "82":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(273,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Fire
			if event == "83":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(274,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Fury
			if event == "84":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(275,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Concentration
			if event == "85":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(276,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Light
			if event == "86":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(277,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Aqua Guard
			if event == "87":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(307,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Earth Guard
			if event == "88":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(309,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Vampire
			if event == "89":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(310,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Protection
			if event == "90":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(311,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Siren's Dance 
			if event == "91":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(365,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Dance of Shadow
			if event == "92":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(366,1).getEffects(st.getPlayer(),st.getPlayer())
				return "8.htm"		
				st.setState(COMPLETED)

			#Song of Earth
			if event == "93":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(264,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Life
			if event == "94":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(265,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Water
			if event == "95":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(266,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Warding
			if event == "96":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(267,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Wind
			if event == "97":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(268,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Hunter
			if event == "98":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(269,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Invocation
			if event == "99":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(270,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Vitality
			if event == "100":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(304,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Vengeance
			if event == "101":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(305,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Flame Guard
			if event == "102":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(306,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Storm Guard
			if event == "103":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(308,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Meditation
			if event == "104":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(363,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Champion
			if event == "105":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(364,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Song of Renewal
			if event == "106":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(349,1).getEffects(st.getPlayer(),st.getPlayer())
				return "9.htm"		
				st.setState(COMPLETED)

			#Fighter Buffers
			if event == "107":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().stopAllEffects()
				SkillTable.getInstance().getInfo(1040,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1036,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1068,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1045,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1087,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1242,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1240,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1086,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1077,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1204,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1363,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(264,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(267,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(268,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(304,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(269,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(349,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(271,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(274,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(275,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1323,1).getEffects(st.getPlayer(),st.getPlayer())
				return "1.htm"
				st.setState(COMPLETED)

			#Mage Buffers
			if event == "108":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().stopAllEffects()
				SkillTable.getInstance().getInfo(1040,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1035,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1036,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1204,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1048,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1085,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1059,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1303,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1078,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(264,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(268,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(267,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(269,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(304,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(349,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(273,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(276,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(365,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1363,1).getEffects(st.getPlayer(),st.getPlayer())
				SkillTable.getInstance().getInfo(1323,1).getEffects(st.getPlayer(),st.getPlayer())
				return "1.htm"			
				st.setState(COMPLETED)

			if event == "109":
				st.takeItems(ADENA_ID,0)
				return "1.htm"		
				st.setState(COMPLETED)

			#Cancel
			if event == "110": 
				st.getPlayer().stopAllEffects()
				return "1.htm"
				st.setState(COMPLETED)

                        #Noblesse Blessing
			if event == "111":
				st.takeItems(ADENA_ID,0)
				SkillTable.getInstance().getInfo(1323,1).getEffects(st.getPlayer(),st.getPlayer())
				return "1.htm"
				st.setState(COMPLETED)	

            		#Restore CP
			if event == "112":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().restoreCP()
				return "1.htm"
				st.setState(State.COMPLETED)	
				
            		#Restore HP
			if event == "113":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().restoreHP()
				return "1.htm"
				st.setState(State.COMPLETED)

           		#Restore MP
			if event == "114":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().restoreMP()
				return "1.htm"
				st.setState(State.COMPLETED)

                        #Restore CP/HP/MP
			if event == "115":
				st.takeItems(ADENA_ID,0)
				st.getPlayer().setCurrentCp(st.getPlayer().getMaxCp())
				st.getPlayer().setCurrentHp(st.getPlayer().getMaxHp())
				st.getPlayer().setCurrentMp(st.getPlayer().getMaxMp())
				return "1.htm"
				st.setState(State.COMPLETED)	

				
			if htmltext != event:
				st.setState(COMPLETED)
				st.exitQuest(1)
		return htmltext


	def onTalk (self,npc,player):
	   st = player.getQuestState(qn)
	   htmltext = "<html><head><body>I have nothing to say to you</body></html>"
	   st.setState(STARTED)
	   return InitialHtml

QUEST       = Quest(QuestId,str(QuestId) + "_" + QuestName,QuestDesc)
CREATED=State('Start',QUEST)
STARTED=State('Started',QUEST)
COMPLETED=State('Completed',QUEST)

QUEST.setInitialState(CREATED)

for npcId in NPC:
 QUEST.addStartNpc(npcId)
 QUEST.addTalkId(npcId)
