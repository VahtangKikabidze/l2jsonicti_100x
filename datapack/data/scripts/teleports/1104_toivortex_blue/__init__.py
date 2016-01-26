import sys

from com.l2jfrozen.gameserver.model.actor.instance import      L2PcInstance
from com.l2jfrozen.gameserver.model.quest        import State
from com.l2jfrozen.gameserver.model.quest        import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
qn = "1104_toivortex_blue"

#print "1104. Toivortex blue"
BLUE_DIMENSION_STONE    = 15003
BLUE_DIMENSION_STONE    = 20313
BLUE_DIMENSION_STONE    = 20314
BLUE_DIMENSION_STONE    = 20315
BLUE_DIMENSION_STONE    = 20316
BLUE_DIMENSION_STONE    = 20317



class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (Self,npc,player):
   st = player.getQuestState(qn)
   npcId = npc.getNpcId()
   if npcId in [ 15003 ] :
     if st.getQuestItemsCount(BLUE_DIMENSION_STONE) >= 1 :
       st.takeItems(15003,5)
       st.takeItems(20313,1)
       st.takeItems(20314,1)
       st.takeItems(20315,1)
       st.takeItems(20316,1)
       st.takeItems(20317,1)
       st.giveItems(20318,1)
       st.exitQuest(1)
       return
     else :
       st.exitQuest(1)
       return "1.htm"

QUEST       = Quest(1104,qn,"Teleports")
CREATED     = State('Start',QUEST)

QUEST.setInitialState(CREATED)

for i in [15003] :
   QUEST.addStartNpc(i)
   QUEST.addTalkId(i)
