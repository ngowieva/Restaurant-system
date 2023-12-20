from nltk.tokenize import word_tokenize # nltk(natural language toolkit)
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt') #installing this specific resource so that NLTK can use it for tokenization tasks.

statiment_words =['what','where','who','when','name','is','do','does','which','are','could','would'
                  ,'should','has','whom','whose',"don't"]
sentence=input("Enter a Sentence :\n")
sentence=sentence.lower()
sentence =word_tokenize(sentence)
if any(x in sentence[0]for x in statiment_words):
    print("This is the question")
else:
    print("This is not a question")