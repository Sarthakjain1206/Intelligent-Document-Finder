import pickle
import numpy as np
print("Downloading...")
import nltk
nltk.download('punkt')
nltk.download('words')
nltk.download('wordnet')
nltk.download('chunk')
nltk.download('corpus')
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('treebank')
nltk.download('conll2000')
print("All external dependencies of nltk is downloaded..")

print("Extracting Word Embeddings..")

def load_word_embeddings():
    global word_embeddings
    word_embeddings = {}
    f = open(r'DataBase\\glove.6B.100d.txt', encoding="utf-8")
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()

load_word_embeddings()

pickle.dump(word_embeddings,open("word_embeddings.json","wb"))
print("Word Embeddings has been extracted, and saved to word_embeddings.json file..")


