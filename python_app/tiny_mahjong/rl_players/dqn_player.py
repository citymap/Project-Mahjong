#!/usr/bin/env python3

#  Copyright 2017 Project Mahjong. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from model_generator import tiny_mahjong_dqn_model
from double_dqn import DoubleDQN
from dqn_interface import *

from game import *

DQN_WEIGHTS_FILE = "tm_dqn_weights.h5"

WIN_REWARD = 1.0
DISCARD_REWARD = 0.0


class DDQNTinyMahjong(DoubleDQN):
    def __init__(self, mode, load=True):
        DoubleDQN.__init__(self, action_count=5, weights_file_path=DQN_WEIGHTS_FILE,
                           mode=mode, load_previous_model=load)

    @staticmethod
    def _pre_process(input_data):
        reshaped_input = np.array([])
        for tile in input_data:
            binarized = [0] * 18
            binarized[int(tile) - 1] = 1
            if reshaped_input.size == 0:
                reshaped_input = np.array(binarized)
            else:
                reshaped_input = np.append(reshaped_input, binarized, axis=0)
        reshaped_input = reshaped_input.reshape(1, 5, 18, 1)
        return reshaped_input

    @staticmethod
    def _create_model():
        return tiny_mahjong_dqn_model()


class DQNPlayer(Player):
    def __init__(self, name, mode):
        Player.__init__(self, name)
        self._mode = mode

        self._dqn_model = DDQNTinyMahjong(mode)

        self._prev_hand = None
        self._prev_action = None

        self._win_rounds = 0
        self._drain_rounds = 0

        self._total_rounds = 0

    def initial_hand_obtained(self):
        Player.initial_hand_obtained(self)
        self._prev_hand = None
        self._prev_action = None

        self._total_rounds += 1

    def tile_picked(self):
        Player.tile_picked(self)
        training = self._prev_hand is not None and self._mode == TRAIN
        if self.test_win():
            if training:
                self._dqn_model.notify_reward(WIN_REWARD)
                self._dqn_model.append_memory_and_train(self._prev_hand,
                                                        self._prev_action,
                                                        WIN_REWARD,
                                                        self.hand,
                                                        True)
            return WIN, -1
        else:
            if training:
                self._dqn_model.notify_reward(DISCARD_REWARD)
            action = self._dqn_model.make_action(self.hand)
            if training:
                self._dqn_model.append_memory_and_train(self._prev_hand,
                                                        self._prev_action,
                                                        DISCARD_REWARD,
                                                        self.hand,
                                                        False)
            self._prev_hand = self.hand
            self._prev_action = action
            return DISCARD, action

    def game_ends(self, win, drain=False):
        Player.game_ends(self, win, drain)

        # Summary.
        if win:
            self._win_rounds += 1
        if drain:
            self._drain_rounds += 1

        self._dqn_model.episode_finished({"Win rate":
                                              self._win_rounds * 1.0 / self._total_rounds,
                                          "Drain rate":
                                              self._drain_rounds * 1.0 / self._total_rounds})

        if self._mode == PLAY:
            print(self.name + ":")
            if win:
                print("Won!")
        elif self._mode == EVAL:
            print("Win rate:", str(self.rounds_won * 100.0 / self._total_rounds) + "%")
        elif self._mode == DEBUG:
            if win:
                print(self.name, "won!")