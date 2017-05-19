# X-Line Extremo Trocar Name

import sys
from com.l2jfrozen.gameserver.datatables.sql import CharNameTable
from com.l2jfrozen.gameserver.model import L2World
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2jfrozen.gameserver.util import Util;

from java.util.regex import Pattern;

# ================================ Custom Name ================================

# X-Line Extremo
# ID Do Npc: 50020 (Special Shop)
NPC = 12300

# X-Line Extremo
# ID Do Coin: 22222 (Ticket Donator)
ITEM_ID = 22222

# X-Line Extremo:
# Contagem do Item
NAME_COUNT = 5

# ============================================================================

class Quest (JQuest) :
    def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

    def onEvent(self,event,st) :
        if event == "1":
            return "1.htm"

        if not CharNameTable.getInstance().doesCharNameExist(event):
            if len(event) >= 3 and len(event) <= 16 and Pattern.matches("[/^([a-zA-Z0-9])+([a-zA-Z0-9\._-]) ?*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$~/]*", event):
                if st.getPlayer().isClanLeader():
                    return u"<html><head><body><center>Voce e Lider de Clan. Nao Pode Mudar de Nome!</center></body></html>"
                if st.getPlayer().getClan():
                    return u"<html><head><body><center>Voce e um membro de clan. Nao Pode Mudar de Nome!</center></body></html>"					
                if st.getQuestItemsCount(ITEM_ID) >= NAME_COUNT:
                    st.takeItems(ITEM_ID,NAME_COUNT)
                    L2World.getInstance().removeFromAllPlayers(st.getPlayer());
                    st.getPlayer().setName(event);
                    st.getPlayer().store();
                    L2World.getInstance().addToAllPlayers(st.getPlayer());
                    st.getPlayer().broadcastUserInfo();
                    return "complete.htm"
                else:
                    return u"<html><head><body><center>Voce Nao tem o item Necessario</body></html>"
            else:
                return u"<html><head><body><center>Try again!</center></body></html>"
        else:
            return u"<html><head><body><center>Nome ja Existe (;</center></body></html>"
        return u"<html><head><body><center>Voce Nao tem o item Necessario</center></body></html>"

    def onTalk (self,npc,player):
        return "index.htm"

QUEST = Quest(1003, "1003_Name", "custom")

QUEST.addStartNpc(NPC)
QUEST.addTalkId(NPC)
