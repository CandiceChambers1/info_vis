import flair
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.nn import Classifier
import sys


# load the model
tagger = Classifier.load('pos')


# make a sentence
sentence = Sentence(sys.argv[1])


# predict NER tags
tagger.predict(sentence)


# print sentence with predicted tags
# print(sentence.get_labels('pos'))


# for token in sentence:
#   print(token)

for label in sentence.get_labels():
  # print(label)
  print(f'"{label.data_point.text}" is classified as "{label.value}" with score {label.score}')

# # load tagger
# # tagger = SequenceTagger.load("flair/chunk-english")
# tagger = Classifier.load('pos')
#
# # make example sentence
# sentence = Sentence(sys.argv[1])
#
# # predict NER tags
# tagger.predict(sentence)
# print(sentence)

# for label in sentence.get_labels():
#     # print(label)
#     print(f'"{label.data_point.text}" is classified as "{label.value}" with score {label.score}')

#
# print("hi")
# # print predicted NER spans
# print(sentence.get_each_embedding("np"))

# print('The following NER tags are found:')
# # iterate over entities and print
# for entity in sentence.get_spans('pos'):
#     print(entity)
