#!/usr/bin/python3

from typing import List

from pandas.core.frame import DataFrame #class

from portfolioDescription.portfolio1MethDescription import Portfolio1MethDescription #class
from portfolioDescription.portfolio1AggrDescription import Portfolio1AggrDescription #class

from evaluationTool.aEvalTool import AEvalTool #class
from evaluationTool.evalToolBanditTS import EvalToolBanditTS #class

from input.inputAggrDefinition import InputAggrDefinition, ModelDefinition  # class

from input.InputRecomDefinition import InputRecomDefinition #class

from portfolioDescription.aPortfolioDescription import APortfolioDescription #class

from input.batchML1m.aML1MConfig import AML1MConf #function


def jobBanditTS(batchID:str, divisionDatasetPercentualSize:int, uBehaviour:str, repetition:int):

        aConf:AML1MConf = AML1MConf(batchID, divisionDatasetPercentualSize, uBehaviour, repetition)

        rIDs, rDescs = InputRecomDefinition.exportPairOfRecomIdsAndRecomDescrs(aConf.datasetID)

        pDescr:Portfolio1AggrDescription = Portfolio1AggrDescription(
                "BanditTS", rIDs, rDescs, InputAggrDefinition.exportADescBanditTS())

        evalTool:AEvalTool = EvalToolBanditTS()
        model:DataFrame = ModelDefinition.createBanditModel(pDescr.getRecommendersIDs())

        aConf.run(pDescr, model, evalTool)