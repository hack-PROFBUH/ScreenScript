from transformers import pipeline

text_generator = pipeline('text-generation', model='gpt2')

text = text_generator("Your prompt here", max_length=100)[0]['generated_text']

print(text)
