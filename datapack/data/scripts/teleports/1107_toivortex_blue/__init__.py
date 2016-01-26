import sys
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
qn = "1107_toivortex_blue"

#print "1107. Toivortex blue"
BLUE_DIMENSION_STONE    = 22222



class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (Self,npc,player):
   st = player.getQuestState(qn)
   npcId = npc.getNpcId()
   if npcId in [ 15023 ] :
     if st.getQuestItemsCount(BLUE_DIMENSION_STONE) >= 10:
           player.setPkKills(0)
           return "1.htm"

QUEST       = Quest(1107,qn,"Teleports")
CREATED     = State('Start',QUEST)

QUEST.setInitialState(CREATED)

for i in [15023] :
   QUEST.addStartNpc(i)
   QUEST.addTalkId(i)
