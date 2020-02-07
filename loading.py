"""this module aims at loading data necessary for evaluation of Semantic Search against Business labelled data"""

import os
import json

DATA_FOLDER = "./data"

def load_eval_data(eval_data_file_name):
    """load the evaluation set built from datafiller"""
    eval_file = os.path.join(DATA_FOLDER, eval_data_file_name)
    with open(eval_file,  "r") as f:
        eval_data = json.load(f)
    return eval_data

def load_content(content_file_name):
    """load the 'content' dataset made of 1.7 documents to rank from"""
    content_file = os.path.join(DATA_FOLDER, content_file_name)
    with open(content_file, "r") as f:
        content_data = json.load(f)
    return content_data
    


if __name__ == "__main__":
    content_slugs = load_content("content.json")
    eval_data = load_eval_data("data_filter_ready.json")
     
    assert len(eval_data) == 156, "size not correct"
    assert len(content_slugs) == 1757, "size not correct"
    assert list(eval_data[0].keys()) == ['title', 'examples'], "present keys are not correct"
    assert list(content_slugs[0].keys()) == ["title", "text", "slug"], "present keys are not correct"
    print("sucessfull loading...")