# ---------------------------------------------------------------
# Project Name: short-activist-report
# Created by: Daglox Kankwanda
# Username: DanGlChris
# Creation Date: October 21, 2023
#
# Copyright: All rights reserved
# ---------------------------------------------------------------

import nltk
from nltk.corpus import stopwords
import re
import string

nltk.download('stopwords')
nltk.download('punkt')

stopwords_lm = stopwords.words('english')

superwords = ['about', 'itself', 'by', 'just', 'won', "she's", 'himself', 'themselves', 'these', 'below', 'of', 'too', 's',
              "shan't", 're', 'didn', 'against', 'and', 'been', 'if', 'from', 'whom', "couldn't", 'the', 'each', 'so', 'can',
              'further', 'does', "won't", 'need', 'we', "mustn't", 'ours', "should've", "that'll", 'wasn', 'until', 'with',
              'she', 'after', 've', 'ourselves', 'only', "you've", 'how', "wasn't", "wouldn't", 'our', 'your', 'very', "shouldn't",
              'out', 'other', 'aren', 'own', 'had', 'herself', 'as', 'an', "you'd", 'some', 'which', 'm', 'him', 'myself', 'you',
              'such', 'off', "doesn't", 'have', 'hasn', 'mustn', 'her', "you're", "aren't", 'them', 'am', 'isn', "didn't", 'he',
              'into', 'up', "hadn't", 'more', 'to', 'not', 'where', 'above', 'what', 'having', 'for', 'any', 'ain', "needn't",
              "weren't", 'hadn', 'yourself', 'y', 'don', 'because', 'o', 'yours', 'my', 'its', 'was', 'his', 'why', 'both',
              "mightn't", 'has', 'shan', 'than', 'it', 'will', "isn't", 'but', 'a', 'down', 'no', 'before', 'their', 'through',
              'under', 'me', "don't", 'were', 'haven', 'mightn', 'weren', "haven't", 'this', 'couldn', 'while', 'at', 'on', 'shouldn',
              'did', "hasn't", 'over', 'i', 'between', 'those', 'doing', 'hers', 'or', 'll', 'when', 'are', 'most', 'be', 'there',
              'doesn', 'again', "it's", 'same', 'during', 'now', 'in', 'few', 't', 'is', 'nor', 'yourselves', 'then', 'they', 'all',
              'once', 'here', 'who', 'theirs', "you'll", 'd', 'ma', 'do', 'should', 'being', 'wouldn', 'that', 'january',
              'february','march','april','may','june','july','august','september','october','november','december']

stopwords_lm.extend(superwords)

def manipulate(val):
  tokens = val.split(" ") #word_tokenize()
  filtered_tokens = [word for word in tokens if word not in stopwords_lm]
  return filtered_tokens

def tokenizer_text(text):
  text = " ".join([re.sub(r'[&),_(\']', " ", i) for i in text.split(" ")])
  text = text.lower()
  text = " ".join([re.sub(r'http\S+|www\S+|\S+@\S+|\d+|[' + re.escape(string.punctuation) + r']|\s+', " ", i) for i in text.split(" ")])
  text = " ".join([re.sub(r'\…|"|“|”|‘', " ", i) for i in text.split(" ")])
  text = " ".join(manipulate(text))
  text = " ".join([re.sub(r"’s\b|’\b|’|》|", "", i) for i in text.split(" ")])
  text = text.replace("’", "")
  text = " ".join([re.sub(r'[^a-zA-Z ]', " ", i) for i in text.split(" ")])
  text = " ".join([i for i in text.split(" ") if 3 <len(i) < 20])
  text = [i for i in text.split(" ") if 3 <len(i) < 20]
  text = " ".join(text)

  return text