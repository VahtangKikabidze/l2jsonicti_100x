import sys

from com.l2jfrozen.gameserver.model.actor.instance import      L2PcInstance
from com.l2jfrozen.gameserver.model.quest        import State
from com.l2jfrozen.gameserver.model.quest        import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
qn = "1106_toivortex_blue"

#print "1106. Toivortex blue"
BLUE_DIMENSION_STONE    = 7586



class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (Self,npc,player):
   st = player.getQuestState(qn)
   npcId = npc.getNpcId()
   if npcId in [ 15007 ] :
     if st.getQuestItemsCount(BLUE_DIMENSION_STONE) >= 1 :
       st.takeItems(7586,1)
       st.giveItems(57,60000)
       st.exitQuest(1)
       return
     else :
       st.exitQuest(1)
       return "1.htm"

QUEST       = Quest(1106,qn,"Teleports")
CREATED     = State('Start',QUEST)

QUEST.setInitialState(CREATED)

for i in [15007] :
   QUEST.addStartNpc(i)
   QUEST.addTalkId(i)
