from nltk.tokenize import word_tokenize # nltk(natural language toolkit)
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt') #installing this specific resource so that NLTK can use it for tokenization tasks.

statiment_words =['what','where','who','when','name','is','do','does','which','are','could','would'
                  ,'should','has','whom','whose',"don't","why"]
print("THIS IS THE PROGRAM TO TEST IF SENTENCE IS QUESTION OR NOT")
sentence=input("Enter English Sentence Only:\n")
#allow the input sentence to be lower case
sentence=sentence.lower()
sentence =word_tokenize(sentence)
if any(x in sentence[0]for x in statiment_words):
    print("This is the question")
else:
    print("This is not a question")
    