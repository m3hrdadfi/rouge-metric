from datasets import load_metric
from pprint import pprint

metric = load_metric("./rouge")

references = [
    "The quick brown fox jumps over the lazy dog"
]

predictions = [
    "The quick brown fox jumps over the lazy dog"
]

result = metric.compute(predictions=predictions, references=references)
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
pprint(result)

references = [
    "The quick brown fox jumps over the lazy dog"
]

predictions = [
    "The quick black cat jumps over the lazy fox"
]

result = metric.compute(predictions=predictions, references=references)
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
pprint(result)
