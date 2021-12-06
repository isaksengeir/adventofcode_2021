#! /usr/bin/env python3
import numpy as np


class LanternFish:
    def __init__(self, internal_timer=8):
        self._timer = internal_timer
        self._kids = 0

    def new_day(self):
        if self._timer == 0:
            self.create_new_fish()
            return True
        self._timer -= 1
        return False

    def create_new_fish(self):
        self._kids += 1
        self.reset_timer()

    def reset_timer(self):
        self._timer = 6

    @property
    def timer(self):
        return self._timer

    @property
    def kids(self):
        return self._kids


class Fishes():
    def __init__(self, init_fishes):
        self.init_fishes = init_fishes
        self._fishes = list()
        for i in init_fishes:
            self.new_fish(timer=i)

    def init_population(self):
        self._fishes.clear()
        for i in self.init_fishes:
            self.new_fish(timer=i)

    def run_simulaiton(self, days=18):
        self.init_population()

        for day in range(1, days + 1):
            fishes_to_append = 0
            for i in range(self.count_fishes):
                new_fish = self.fishes[i].new_day()
                if new_fish:
                    fishes_to_append += 1
            for n in range(fishes_to_append):
                self.new_fish(timer=8)

        return self.count_fishes

    def new_fish(self, timer=8):
        fish = LanternFish(internal_timer=timer)
        self.fishes = fish

    @property
    def fishes(self):
        return self._fishes

    @property
    def count_fishes (self):
        return len(self.fishes)

    @fishes.setter
    def fishes(self, value):
        self._fishes.append(value)


def init_counter(fishes):
    fish_counter = dict()
    for fish in fishes:
        if fish not in fish_counter.keys():
            fish_counter[fish] = 0
        fish_counter[fish] += 1
    return fish_counter


def sim_growth_simple(days, fish_counter):
    for day in range(1, days + 1):
        newbies = dict()
        for count_grup in fish_counter.keys():
            if count_grup not in newbies:
                newbies[count_grup] = 0
            group_size = fish_counter[count_grup]
            if count_grup == 0:
                if 6 not in newbies:
                    newbies[6] = 0
                if 8 not in newbies:
                    newbies[8] = 0
                newbies[6] += group_size
                newbies[8] += group_size
            else:
                if count_grup - 1 not in newbies:
                    newbies[count_grup - 1] = 0
                newbies[count_grup - 1] += group_size

        fish_counter = newbies

    return sum(fish_counter.values())


if __name__ == "__main__":
    simdays = 256
    init_fishes = np.loadtxt("data.txt", delimiter=",", dtype=int)
    #init_fishes = [3, 4, 3, 1, 2]

    simfish = Fishes(init_fishes=init_fishes)

    print(f"PART1: There are {simfish.run_simulaiton(80)} fishes after 80 days!")

    # OK, my class approach is waaaay to slow - need to do something easier:

    fc = init_counter(init_fishes)
    part2 = sim_growth_simple(days=256, fish_counter=fc)
    print(part2)



