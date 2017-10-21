import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/sydshir/Desktop/Code'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
pillar = nltk.Text(wordlists.words('cityandthepillar.txt'))
pillar[:10]
pillar.concordance('gay')
list(nltk.bigrams(pillar))

#Frequency Distribution Calculator
fdist1 = FreqDist(pillar)
print(fdist1)
fdist1.most_common(50)
fdist1['gay']

#Bigrams Generator 
def generate_model(cfdist, word, num=1):
   for i in range(num):
      print(word, end=' ')
      word = cfdist[word].max()

text = nltk.Text(wordlists.words('cityandthepillar.txt'))
bigrams = nltk.bigrams(pillar)
cfd = nltk.ConditionalFreqDist(bigrams)
cfd['gay']
generate_model(cfd, 'gay')

