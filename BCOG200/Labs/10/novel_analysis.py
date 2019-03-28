import os

import nltk

""" Comment this code """
title_list = []
text_list = []
fdist_list = []

input_directory = 'books/'
book_file_list = os.listdir(input_directory)

interesting_words = ['hello', 'world', 'and', 'these', 'are',
                     'the', 'ten', 'words', 'I', 'pick']

title_max_length = 24
number_length = 10

title = ('{0: <%d}' % title_max_length).format('Title')
for word in interesting_words:
    title += ('{0: <%d}' % number_length).format(word)
print(title)

for book in book_file_list:
    if book[0] == '.':
        book_file_list.remove(book)
    else:
        title = book[:-4]
        title_list.append(title)
        f = open(input_directory + book)
        book_string = f.read()
        tokens = nltk.word_tokenize(book_string)
        text = nltk.Text(tokens)
        text_list.append(text)
        fdist = nltk.FreqDist(text)
        fdist_list.append(fdist)
        s = ('{0: <%d}' % title_max_length).format(title)
        for word in interesting_words:
            s += ('{0: <%d}' % number_length).format(fdist[word])
        print(s)

"""
USING NLTK:
    0. create a frequency distribution nltk object for each text and store in 
    the fdist list
    1. print out the number of total and unique words in each book
    2. pick 10 words you are interested in and print out how many times each
        occurred in each book in a nice, organized formatted table
    3. wait for instructions for your final task
"""
