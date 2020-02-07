import torch
from transformers import FlaubertModel, FlaubertTokenizer
from preprocess import preprocess
from sklearn.metrics.pairwise import cosine_similarity

from tqdm import tqdm
modelname = 'flaubert-base-uncased' 

# Load pretrained model and tokenizer
flaubert, log = FlaubertModel.from_pretrained(modelname, output_loading_info=True)
flaubert_tokenizer = FlaubertTokenizer.from_pretrained(modelname, do_lowercase=True)


def get_flo_vec(q):
    query = preprocess(q, lower=True)
    token_ids = torch.tensor([flaubert_tokenizer.encode(query)])
    last_layer = flaubert(token_ids)[0][: ,1:-1, :]
    return last_layer.detach().numpy().mean(axis=1)

def build_flo_mat(titles_processed):
    f_mat = [get_flo_vec(t).squeeze() for t in tqdm(titles_processed)]
    return f_mat


class Predictor():
    def __init__(self, titles):
        self.mat = self._build_flo_mat(titles)
        self.name = "FlaubertModel"

    def _build_flo_mat(self, titles_processed):
        f_mat = [get_flo_vec(t).squeeze() for t in tqdm(titles_processed, desc="creating document matrix")]
        return f_mat
    
    def predict(self, query, slugs, n=10):
        vec = get_flo_vec(query)
        topn = cosine_similarity(vec, self.mat).squeeze().argsort()[::-1][:n]
        return [slugs[t] for t in topn]

if __name__ == "__main__":
    print(get_flo_vec("hello"))