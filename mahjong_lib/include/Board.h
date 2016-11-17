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

#ifndef MAHJONG_LIB_BOARD_H
#define MAHJONG_LIB_BOARD_H

#include <string>
#include <vector>

#include "Hand.h"
#include "Player.h"

namespace mahjong {

class Board {
 public:
    Board(std::vector<Player> players, bool enableDora, int doraStackSize);

    void setup();

 private:
    int mPlayerCount;
    std::vector<Player> mPlayers;
    bool mEnableDora;
    int mDoraStackSize;

    // Round Wind.
};

} // namespace mahjong.

#endif // MAHJONG_LIB_BOARD_H
