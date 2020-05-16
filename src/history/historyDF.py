#!/usr/bin/python3

from typing import List
from pandas.core.series import Series #class

import pandas as pd

from history.aHistory import AHistory #class

from userBehaviourDescription.userBehaviourDescription import UserBehaviourDescription #class


class HistoryDF(AHistory):

    ITEM_ID = "itemID"
    RECOMMENDED_IDS = "recommendedIds"
    PROBS_OF_OBSERVATION = "probabilityOfObservation"

    def __init__(self):

        historyData:pd.DataFrame = []
        self._historyDF:pd.DataFrame = pd.DataFrame(historyData, columns=[self.ITEM_ID, self.RECOMMENDED_IDS, self.PROBS_OF_OBSERVATION])


    def addRecommendation(self, itemID:int, recommendedItemIDs:List[int], uObservation:List[bool]):

        new_row:pd.Series = pd.Series({self.ITEM_ID:itemID, self.RECOMMENDED_IDS:recommendedItemIDs, self.PROBS_OF_OBSERVATION:uObservation})
        self._historyDF = self._historyDF.append(new_row, ignore_index=True)


    def getIgnoringValue(self, itemID:int, numberOfItems:int=20, lengthOfHistory:int=20):

        def valueOfIgnoring(historyIndex:int):
            rowI:Series = self._historyDF.iloc[historyIndex]

            itemIDs:List[int] = rowI[self.RECOMMENDED_IDS]
            probsOfObserv:List[float] = rowI[self.PROBS_OF_OBSERVATION]

            if itemID not in itemIDs:
                return 0.0

            indexI:int = itemIDs.index(itemID)
            return probsOfObserv[indexI]

        return sum(map(valueOfIgnoring, range(len(self._historyDF.index))))


    def print(self):
        print(self._historyDF.head(10))