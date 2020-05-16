#!/usr/bin/python3

from typing import List

import numpy as np

from userBehaviourDescription.userBehaviourDescription import UserBehaviourDescription #class


class UserBehaviourSimulator:

    def simulate(self, uBehaviourDesc:UserBehaviourDescription, numberOfItems:int):

        maxProbOfObserv:List[float] = uBehaviourDesc.getProbabilityOfBehavior(numberOfItems)
        #print("maxProbOfObserv: " + str(maxProbOfObserv))

        probabilitiesGenerated:List[float] = list(map(lambda max: np.random.uniform(low=0.0, high=max), maxProbOfObserv))
        #print("probabilitiesGenerated: " + str(probabilitiesGenerated))

        return probabilitiesGenerated
