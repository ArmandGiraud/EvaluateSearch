
"""this module defines a class for evaluation"""
from metrics import discounted_cumulative_gain, mean_reciprocal_rank, find_precision_k, find_recall_k
import numpy as np
from tqdm import tqdm
from collections import defaultdict
from typing import Callable

class Evaluator():

    def __init__(self, eval_data, content):
        self._eval_data = eval_data
        self.slugs = [t["slug"] for t in content]
        self.titles = [t["title"] for t in content]


    def evaluate_on_df(self, predictor, k: int=5):
        """evaluate on datafiller"""

        # instantiate the prredictor class which contains a name attribute and preict metho
        p = predictor(self.titles)
        # eval procedure


        
        scores = defaultdict(list)
        # loop oveer eval_dataset
        for line in tqdm(self._eval_data, desc = "Scoring Documents"):
            dcg, mrr, recall, precision = [], [], [], []
            # loop over variants queries of the doc
            for example in line["examples"]:
                ### perform prediction using the predictor and the query
                y_pred = p.predict(example["query"], self.slugs, n = k)
                ###
                y_true = example["y_true"]
                y_score = example["y_score"]
                
                ## compute metrics based on the slugs returned and the ground truth
                dcg.append(discounted_cumulative_gain(y_score, y_true, y_pred, k = k))
                mrr.append(mean_reciprocal_rank(y_pred, y_true))
                precision.append(find_precision_k(y_pred, y_true, k = k))
                recall.append(find_recall_k(y_pred, y_true, k = k))

            # average scores over the variants per document
            scores["dcg"].append(np.mean(dcg))
            scores["mrr"].append(np.mean(mrr))
            scores["precision"].append(np.mean(precision))
            scores["recall"].append(np.mean(recall))
        
        # average the scores over all documents
        print("#"*50)
        print("evaluation for {}".format(p.name))
        print("--"*25)
        print("dcg:", np.nanmean(scores["dcg"]))
        print("mrr:", np.nanmean(scores["mrr"]))
        print("precision:", np.nanmean(scores["precision"]))
        print("recall:" ,np.nanmean(scores["recall"]))
        print("#"*50)
        return scores
    
    