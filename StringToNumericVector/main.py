from transformers import AutoTokenizer 

line = 'What color is the undoubtedly the most beautiful color in the world?'

model_name = 'google/flan-t5-base' # string here is the hugging face model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokens = tokenizer.tokenize(line, return_tensors='pt')
print(tokens)
# ids = tokenizer.convert_tokens_to_ids(tokens)
# print(ids)