#!/usr/bin/python3

from typing import List

from aggregation.aggrBanditTS import AggrBanditTS #class

import pandas as pd


def test01():
    print("Test 01")

    print("Running AggrBanditTSRun:")

    # number of recommended items
    N = 120

    # method results, items=[1,2,4,5,6,7,8,12,32,64,77]
    methodsResultDict = {
        "metoda1": pd.Series([0.2, 0.1, 0.3, 0.3, 0.1], [32, 2, 8, 1, 4], name="rating"),
        "metoda2": pd.Series([0.1, 0.1, 0.2, 0.3, 0.3], [1, 5, 32, 6, 7], name="rating"),
        "metoda3": pd.Series([0.3, 0.1, 0.2, 0.3, 0.1], [7, 2, 77, 64, 12], name="rating")
    }
    # print(methodsResultDict)

    # methods parametes
    methodsParamsData = [['metoda1', 5, 10, 1, 1], ['metoda2', 5, 12, 1, 1], ['metoda3', 6, 13, 1, 1]]
    methodsParamsDF = pd.DataFrame(methodsParamsData, columns=["methodID", "r", "n", "alpha0", "beta0"])
    methodsParamsDF.set_index("methodID", inplace=True)
    # print(methodsParamsDF)

    aggr:AggrBanditTS = AggrBanditTS({})

    # itemIDs:List[tuple] = aggr.runWithResponsibility(methodsResultDict, methodsParamsDF, N)
    itemIDs:List[tuple] = aggr.run(methodsResultDict, methodsParamsDF, N)
    print(itemIDs)


def main():
    print("D'Hondt algorithm")

    test01()
    # [(1, 'metoda1'), (32, 'metoda1'), (2, 'metoda1'), (8, 'metoda1'), (6, 'metoda2'), (4, 'metoda1'), (7, 'metoda3'), (5, 'metoda2'), (64, 'metoda3'), (77, 'metoda3'), (12, 'metoda3')]


if __name__ == "__main__":
    main()