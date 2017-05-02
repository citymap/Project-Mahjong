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

import sys

sys.path.append("../")

from double_dqn import *

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


class DQNCartpole(DoubleDQN):
    def __init__(self, action_count=2, weights_file_path="cartpole_weights.h5"):
        DoubleDQN.__init__(self, action_count, weights_file_path,
                           target_update_interval=1000)

    @staticmethod
    def _create_model():
        model = Sequential()
        model.add(Dense(20, input_shape=(4, ), activation="relu"))
        model.add(Dense(2, activation='linear'))
        model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.001), metrics=['accuracy'])

        return model

    @staticmethod
    def _pre_process(input_data):
        return input_data.reshape(1, 4)