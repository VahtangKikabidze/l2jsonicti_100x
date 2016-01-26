import sys

from com.l2jfrozen.gameserver.model.actor.instance import      L2PcInstance
from com.l2jfrozen.gameserver.model.quest        import State
from com.l2jfrozen.gameserver.model.quest        import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
qn = "1103_toivortex_blue"

#print "1103. Toivortex blue"
BLUE_DIMENSION_STONE    = 20306



class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (Self,npc,player):
   st = player.getQuestState(qn)
   npcId = npc.getNpcId()
   if npcId in [ 15000 ] :
     if st.getQuestItemsCount(BLUE_DIMENSION_STONE) >= 1 :
       st.takeItems(20306,1)
       st.giveItems(6657,1)
       st.giveItems(6658,1)
       st.giveItems(6659,1)
       st.giveItems(6660,1)
       st.giveItems(6656,1)
       st.exitQuest(1)
       return
     else :
       st.exitQuest(1)
       return "1.htm"

QUEST       = Quest(1103,qn,"Teleports")
CREATED     = State('Start',QUEST)

QUEST.setInitialState(CREATED)

for i in [15000] :
   QUEST.addStartNpc(i)
   QUEST.addTalkId(i)
