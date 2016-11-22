//
//  Copyright © 2016 Project Mahjong. All rights reserved.
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//

#include <Board.h>

#include <iostream>

using std::string;

using mahjong::Hand;
using mahjong::Wind;
using mahjong::Player;

void Player::setupPlayer(int ID,
                         Wind seatPosition,
                         mahjong::Hand initialHand) {
    mID = ID;
    mSeatPosition = seatPosition;
    mHand = initialHand;
}

void Player::shiftSeatPosition() {
    mSeatPosition == North ? mSeatPosition = East :
       mSeatPosition = static_cast<Wind>(static_cast<int>(mSeatPosition) + 1);
}

mahjong::Action Player::onTurn(bool isMyTurn, Tile tile) {
    std::cerr << "Virtual function, do not call.";
    return Action();
}

void Player::onOtherPlayerMakeAction(Player *player, mahjong::Action action) {
    std::cerr << "Virtual function, do not call.";
}