"""module for preprocessing the query"""

from nltk.corpus import stopwords
import unicodedata

def load_stops():
    """load stop words for removal"""
    stops = stopwords.open("french").read().splitlines()
    more_stops = ["travail", "travailler", "travaille"]
    stops.extend(more_stops)
    stops = set(stops)
    return stops

def preprocess(string: str, lower: bool = False):
    """perform actual cleaning on a string with optional lowercasing"""
    stops = load_stops()
    tokens = string.split()
    tokens_filtered = [
        t for t in tokens if t not in stops ]
    if not lower:
        return " ".join(tokens_filtered)
    else:
        return " ".join(tokens_filtered).lower()


def strip_accents(s: str):
    """remove accents"""
    return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')

if __name__ == "__main__":
    print(preprocess(" droit du travail")) == "droit", "problem in processing"