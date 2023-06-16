import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.casefold() not in stop_words]
    count = Counter(filtered_text)
    return count.most_common(10)


"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) 

text = ""
word_tokens = word_tokenize(text) 
  
filtered_text = [w for w in word_tokens if not w in stop_words] 

print(filtered_text)

"""