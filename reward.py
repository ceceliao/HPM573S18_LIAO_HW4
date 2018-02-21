from enum import Enum
import numpy as np

class coinstate(Enum):
    TAIL=1
    HEAD=0

class game(object):
    def __init__(self, id, coin_prob):
        self._id=id
        self._rnd=np.random
        self._rnd.seed(self._id)
        self._coin_prob=coin_prob
        self._countTail=0
        self._reward=0

    def simulate(self, n_time_steps):
        self._n_time_steps=0

        while self._n_time_steps < n_time_steps:

            if self._rnd.sample()<self._coin_prob:
                self.coinstate = coinstate.TAIL
                self._countTail+=1
                self._n_time_steps+=1

            elif self._rnd.sample() >self._coin_prob:
                self.coinstate=coinstate.HEAD
                self._n_time_steps +=1
                if self._countTail>=2:
                    self._countTail =0
                    self._reward+=1


    def get_reward(self):
        self._reward =self._reward*100-250
        return self._reward


class cohort:
    def __init__(self, id, pop_size, coin_prob):
        self._coins = []
        self._success=[]

        for i in range (pop_size):
            coins = game(id*pop_size+i, coin_prob)
            self._coins.append(coins)

    def simulate(self, n_time_steps):
        for coin in self._coins:
            coin.simulate(n_time_steps)
            value = coin.get_reward()
            if not (value is None):
                self._success.append(value)

    def get_reward(self):
        return sum(self._success)/len(self._success)

