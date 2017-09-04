from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import sys, re, numpy
import nltk
from nltk.tokenize import sent_tokenize
import timeit

start = timeit.default_timer()





data=[]

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

data= open('text.txt').read()
data = re.sub(r"http\S+", " ", data)
data = re.sub(r"none"," ", data)
#data = data.replace(r"N$", "")
#data = re.sub(r"Business"," ", data)
#data = re.sub(r"News","", data)
#data = re.sub(r"N","",data)
#data = re.sub("St.","",data)
data = re.sub('[^a-zA-Z_ ]', "", data)
#data = re.sub('  +',' ',data)
#data = re.sub("\S*\d\S*", "", data).strip()
#data = re.sub(r" s","",data)
# lines=[]
# lines = re.split(r"\.\s*", data)

data = re.split('  ',data)



#pat = ('(?<!Dr)(?<!Esq)\. +(?=[A-Z])')
#data =re.sub(pat,'.\n',data)

thefile = open('cleantext.txt', 'w')
for item in data:
  thefile.write("%s\n" % item)

#print(data)

#print(data)





# list for tokenized documents in loop
texts = []

# loop through document list
for i in data:
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    # add tokens to list
    texts.append(stopped_tokens)

print(texts)

#print(en_stop)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word=dictionary, passes=20)
print(ldamodel.print_topics(num_topics=20, num_words=4))

stop = timeit.default_timer()

print(stop-start)
