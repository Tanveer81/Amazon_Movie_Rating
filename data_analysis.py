import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

%matplotlib inline

with open('Movies_and_TV_5.json') as f:
    raw_data = f.readlines()[0:5]
    
    
