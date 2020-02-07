# Evaluate Semantic Search

These scripts helps evaluate the quality of a ranking model for the [Code du travail Numérique](code.travail.gouv.fr) Search Engine against manually labelled data aka the [Datafiller](https://datafiller.num.social.gouv.fr/).


### Install:
`pip install -r requirements.txt`

### Run on [FlauBert](https://github.com/getalp/Flaubert):

`python eval.py`

### Run on [CamemBert](https://camembert-model.fr/):
`to do`

### Run on [USE](https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/2)
 `to do`

## Evaluate your own model:
 create a new file `yourModel.py` which defines a Predictor class having a predict method
 - given a string query should return k slugs from the slugs parameters
 and a name attribute and param attributes.

 see [Flaubertmodel.py](https://github.com/ArmandGiraud/EvaluateSearch/blob/40e1fb956d93059adfe7f58a54309a516cd9fb71/Flaubertmodel.py#L25) for example
