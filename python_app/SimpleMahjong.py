#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../build_mahjong")
sys.path.append("../../build_players")
sys.path.append("../../build_games")
from libmahjong import *
from libplayers import *
from libgames import *

class StupidPlayer(Player):
    def __init__(self, playerName):
        super(StupidPlayer, self).__init__(playerName)
    def onTurn(self, this, playerID, tile):
        if playerID == this.getID():
            if this.getHand().testWin():
                return Action(ActionState.Win, Tile())

            handData = this.getHand().getData()
            it = 0
            while handData[it].getFlag() != TileFlag.Handed:
                it += 1
            return Action(ActionState.Discard, handData[it])
        else:
            return Action()
    def onOtherPlayerMakeAction(self, playerID, playerName, action):
        return Action()

p1 = makeGreedyPlayer("BOT Greedy 1")
p2 = makeGreedyPlayer("BOT Greedy 2")
#p2 = makeUserInputPlayer("Smart Human")
p3 = makeGreedyPlayer("BOT Greedy 3")
SB = StupidPlayer("SB")
p4 = makePythonPlayer(SB)

game = SimpleGame(p1, p2, p3, p4, 1000)

game.startGame()
