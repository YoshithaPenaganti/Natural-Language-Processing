# Natural-Language-Processing
These codes are related to natural language processing and mainly contains codes related to news articles.
---------ldamodel.py------------ 

This is the model which can be applied on a raw text corpus to find the topics and words

-----Fasttext Model-CBOW---------

This Model is implemented on the list of Json linkedIn files.This code contains extraction of data from json to a python list.Then, I have trained the data using fasttext Cbow model.CBOW is one of the models of Word to Vector representation.The training time of this model is 109 secs.


-----Word2vec.py------------------

This is the Word2vec model applied on Wikicorpus. This model is trained and ready to use which produces a bin file as an output.The model.vec file is produced by this file.

--------model.vec-----------------

This file contains the sentence vectors of all the Wikicorpus trained by Word2vec.py

-----------tfidf.py---------------

This file has the Tfidf model applied on 14 million headlines as documents and gives the top 3 important words as the output. Tfidf model calculates the term frequency and inverse document frequency which gives a final score reflecting the importance of the word to that respective document.




