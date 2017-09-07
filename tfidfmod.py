import math
from textblob import TextBlob as tb
import re



def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
tlist=[]
tlist= open('cleantext.txt').read()
tlist = re.split("\n",tlist)

print(tlist)
bloblist=[]
for i in tlist:

    i=tb(i)
    bloblist.append(i)

file = open('tfidftext.txt', 'w')
for i, blob in enumerate(bloblist):
    print("\nTop words in document ::{}\n".format(blob))
    file.write("\nTop words in document ::{}\n".format(blob))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
         print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
         file.write("\nWord: {}, TF-IDF: {}".format(word, round(score, 5)))
    file.write("\n")
