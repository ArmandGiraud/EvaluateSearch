from loading import load_eval_data, load_content
from Flaubertmodel import Predictor

from evaluator import Evaluator
content_slugs = load_content("content.json")
eval_data = load_eval_data("data_filter_ready.json")

    
titles = [c["title"] for c in content_slugs]
contexts = [c["text"] for c in content_slugs]


if __name__ == "__main__":
    ev = Evaluator(eval_data, content_slugs)
    ev.evaluate_on_df(Predictor)

