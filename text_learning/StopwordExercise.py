import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


#nltk.download()
sw = stopwords.words("english")

stemmer = SnowballStemmer("english")

print(stemmer.stem("unresponse"))