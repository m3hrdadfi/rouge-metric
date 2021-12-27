from datasets import load_metric

metric = load_metric("./rouge")

# Language: en-English
references = ["The quick brown fox jumps over the lazy dog"]
predictions = ["The quick brown fox jumps over the lazy dog"]
result = metric.compute(predictions=predictions, references=references, language="en")
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: English, result: {result}")

references = ["The quick brown fox jumps over the lazy dog"]
predictions = ["The quick black cat jumps over the lazy fox"]
result = metric.compute(predictions=predictions, references=references, language="en")
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: English, result: {result}")

# Language: fa-Persian
references = ["روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد"]
predictions = ["روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد"]
result = metric.compute(predictions=predictions, references=references, language="fa")
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: Persian, result: {result}")

references = ["روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد"]
predictions = ["گربه سیاه سریع از روی روباه تنبل می‌پرد"]
result = metric.compute(predictions=predictions, references=references, language="fa")
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: Persian, result: {result}")

# Language: tr-Turkish
references = ["Yurtta sulh cihanda sulh"]
predictions = ["Yurtta sulh cihanda sulh"]
result = metric.compute(predictions=predictions, references=references, language="tr", use_stemmer=True)
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: Turkish, result: {result}")

references = ["Yurtta sulh cihanda sulh"]
predictions = ["Yurtta barış dünyada barış"]
result = metric.compute(predictions=predictions, references=references, language="tr", use_stemmer=True)
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: Turkish, result: {result}")

# Language: hu-Hungarian
references = ["Aki mer az nyer"]
predictions = ["Aki mer az nyer"]
result = metric.compute(predictions=predictions, references=references, language="hu", use_stemmer=True)
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: Hungarian, result: {result}")

references = ["Aki mer az nyer"]
predictions = ["Aki mer az veszít"]
result = metric.compute(predictions=predictions, references=references, language="hu", use_stemmer=True)
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: Hungarian, result: {result}")
