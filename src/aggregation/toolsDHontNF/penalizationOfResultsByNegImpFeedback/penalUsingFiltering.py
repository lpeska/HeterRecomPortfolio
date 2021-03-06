#!/usr/bin/python3
import random
import itertools

import numpy as np
import pandas as pd

from numpy.random import beta
from typing import List

from pandas.core.frame import DataFrame  # class
from pandas.core.series import Series  # class

from history.aHistory import AHistory #class

from userBehaviourDescription.userBehaviourDescription import UserBehaviourDescription #class
from aggregation.toolsDHontNF.penalizationOfResultsByNegImpFeedback.aPenalization import APenalization #class


# transforming Results Of D'Hont Methods
class PenalUsingFiltering(APenalization):

    def __init__(self, borderNegFeedback:float):
        if type(borderNegFeedback) is not float:
            raise ValueError("Type of borderNegFeedback isn't float.")

        self._borderNegFeedback:float = borderNegFeedback

    # methodsResultDict:dict[int,Series[int,str]]
    def runPenalization(self, userID:int, methodsResultDict:dict, history:AHistory, lengthOfHistory:int):

        def getItemIDs(methIdI:str):
            recommI:Series = methodsResultDict[methIdI]
            itemIDsI:List[int] = recommI.index
            return itemIDsI

        itemsInRecomendationsLL:List[List[int]] = map(getItemIDs, methodsResultDict)
        itemsInRecomendations:List[int] = list(itertools.chain.from_iterable(itemsInRecomendationsLL))

        itemIdsToRemove:List[int] = []
        for itemIdI in itemsInRecomendations:
            valueOfIgnoringI:float = history.getIgnoringValue(userID, itemIdI, limit=lengthOfHistory)
            #print("valueOfIgnoringI: " + str(valueOfIgnoringI))
            if valueOfIgnoringI >= self._borderNegFeedback:
                itemIdsToRemove.append(itemIdI)

        #print("itemIdsToRemove: " + str(itemIdsToRemove))

        methodsResultNewDict:dict = {}
        for methIdI in methodsResultDict.keys():
            ratingsI:Series = methodsResultDict[methIdI]
            ratingsNewI:Series = ratingsI.drop(list(set(ratingsI.keys()) & set(itemIdsToRemove)))
            methodsResultNewDict[methIdI] = ratingsNewI

        return methodsResultNewDict

