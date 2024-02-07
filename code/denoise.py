from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
from tqdm import tqdm

tokenizer = AutoTokenizer.from_pretrained("kfkas/t5-large-korean-P2G")
model = AutoModelForSeq2SeqLM.from_pretrained("kfkas/t5-large-korean-P2G")

data = pd.read_csv('### original data ###')


batch_size = 16

def denoise(batch_texts):
    inputs = tokenizer(batch_texts, padding=True, truncation=True, return_tensors="pt")
    outputs = model.generate(**inputs)
    
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

results = []

for i in tqdm(range(0, len(data), batch_size)):
    batch = data['text'][i:i+batch_size].tolist()
    batch_results = denoise(batch)
    results.extend(batch_results)

data['text'] = results


data.to_csv("### save csv ###", index=False)