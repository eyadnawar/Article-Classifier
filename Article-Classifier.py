import os
from os import path
from collections import Counter
from nltk.corpus import stopwords
from decimal import *

DATA_TRAIN_PATH = 'C:/Users/Lenovo/.PyCharmCE2017.1/config/scratches/ArticleClassifier/bbc_train'
DATA_TEST_PATH  = 'C:/Users/Lenovo/.PyCharmCE2017.1/config/scratches/ArticleClassifier/bbc_test'
DELIMITERS = [',', '.', '!', '?', '/', '&', '-', ':', ';', '@', '"', "'"]
stopWords = open('stop_words.txt', 'r').read().split()
list_of_article_types = [('business',450) , ('entertainment',344),('politics',375),('sport', 454), ('tech',356)]

big_dictionary = {}
big_test_dictionary = {}
dictionary_of_probabilities_for_all_words = {}

for article_type in os.listdir(DATA_TRAIN_PATH):
    article_type_path = path.join(DATA_TRAIN_PATH, article_type)
    article_words = []
    for article in os.listdir(article_type_path):
        article_path = path.join(article_type_path, article)
        with open(article_path) as file:
            text = file.read().split()
            article_words.extend(''.join(c for c in words.lower() if c not in DELIMITERS) for words in text)
    article_counter = Counter(article_words)
    article_counter.pop('', None)
    for stopping_word in stopWords:
        article_counter.pop(stopping_word, None)
    for stopper in set(stopwords.words('English')):
        article_counter.pop(stopper, None)
    big_dictionary[article_type] = article_counter.most_common(70)
#print (big_dictionary)

##Get the vocabulary list ##no duplication in lists
vocabulary = []
for every_type in big_dictionary:
   for every_tuple in big_dictionary[every_type]:
       vocabulary.append(every_tuple[0])
#print (vocabulary)


##Get the n  ##summing all the number of times words occured in a specific article type
the_n_dictionary = {}
count = 0
for every_type in big_dictionary:
    for every_tuple in big_dictionary[every_type]:
        count += every_tuple[1]
    the_n_dictionary[every_type] = count
    count = 0
#print (the_n_dictionary)



def get_the_n(article_type):
    return the_n_dictionary[article_type]



def count_the_n_sub_k(article_type, word):
    for every_tuple in big_dictionary[article_type]:
        if every_tuple[0] == word:
            return every_tuple[1]
    return 0



##Calculate probabilities
def calculate_probability(article_type, word):
     return (count_the_n_sub_k(article_type, word) + 1 ) / (get_the_n(article_type)+ len(vocabulary))



'''
##Compute the probabilities of all words in every article tye
for article_type in os.listdir(DATA_TRAIN_PATH):
    for word in vocabulary:
        dictionary_of_probabilities_for_all_words[article_type] = [(word, calculate_probability(word))]
'''
#print(dictionary_of_probabilities_for_all_words)




defined_list_of_probabilities = []
def add_probabilities_to_a_list(article_type):
    for word in vocabulary:
        defined_list_of_probabilities.append((word, calculate_probability(article_type, word)))
    return defined_list_of_probabilities

#print (add_probabilities_to_a_list('entertainment'))
#print(article_type, '\n', '=============', '\n', word, ':', calculate_probability(article_type,word))
#print(add_probabilities_to_a_list('sport'))
#print(article_type, '\n', '=============', '\n', word, ':', calculate_probability(word))
#print(add_probabilities_to_a_list('sports'))



def search_for_test_word_in_defined_list_of_probabilities(article_type, word):
    for item in add_probabilities_to_a_list(article_type):
        if item[0] == word:
            return item[1]
    return  1 / (get_the_n(article_type) + len(vocabulary))

#print (search_for_test_word_in_defined_list_of_probabilities('entertainment', 'games'))
#print (search_for_test_word_in_defined_list_of_probabilities('entertainment', 'film'))

list_of_words = []
new_list = []
sorted_list = []
def predict_article(article_path):
    list_of_max_prbability_of_article_type = []
    with open(article_path) as my_article:
        words = my_article.read().split()
        list_of_words.extend(''.join(g for g in bing.lower() if g not in DELIMITERS) for bing in words)
    my_counter = Counter(list_of_words)
    my_counter.pop('', None)
    for stopping_word in stopWords:
        my_counter.pop(stopping_word, None)
    for stopping in set(stopwords.words('English')):
        article_counter.pop(stopper, None)
    new_list = my_counter.most_common(15)
    for i in list_of_article_types:
        word_prob = 1
        predict_counter = 0
        article_type = i[0]
        predict_counter = i[1] / 1979
        for word in new_list:
            word_prob = ( Decimal(word_prob) * Decimal(search_for_test_word_in_defined_list_of_probabilities(i[0], word[0])) * Decimal(word[1]) )
        predict_counter = ( Decimal(predict_counter) * Decimal(word_prob) )
        list_of_max_prbability_of_article_type.append((article_type, predict_counter))
        sorted_list = sorted(list_of_max_prbability_of_article_type, key=lambda x: x[1], reverse= True)
        word_prob = 1
        predict_counter = 0
    return (sorted_list)


print(predict_article('ArticleClassifier/bbc_test/sport/481.txt'))


'''
print(predict_article('ArticleClassifier/bbc_test/politics/376.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/377.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/378.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/379.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/380.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/381.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/382.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/383.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/384.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/385.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/386.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/387.txt'))
print(predict_article('ArticleClassifier/bbc_test/politics/388.txt'))
'''

##### 1979

##business = 450
##entertainment = 344
##politics = 375
##sport = 454
##tech = 356

'''
print (predict_article('ArticleClassifier/bbc_test/business/455.txt'))
print (predict_article('ArticleClassifier/bbc_test/sport/472.txt'))
print (predict_article('ArticleClassifier/bbc_test/tech/377.txt'))
print (predict_article('ArticleClassifier/bbc_test/politics/380.txt'))
'''



