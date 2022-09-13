from curses.ascii import isalpha
import sys
import re

# print(sys.argv)

with open(sys.argv[1]) as f:
    # read file
    a = f.read()
    # get number of characters
    nb_characters = len(a)
    print("Number of characters: ", nb_characters)
    # get number of lines
    lines = a.splitlines()
    nb_lines = len(lines)
    print("Number of lines: ", nb_lines)
    # get number of words
    words = re.findall(r"\w+", a)
    nb_words = len(words)
    print("Number of words: ", nb_words)
    # get longest word
    word_len_set = {len(word) for word in words}
    longest_word_len = max(word_len_set)
    longest_word = {word for word in words if len(word) == longest_word_len}
    print("Longest word: ", longest_word)
    # get most frequent words
    # create word-frequency dictionary
    word_freq = dict()
    for word in words:
        word_lower = word.lower()
        if word_lower in word_freq:
            word_freq[word_lower] += 1
        else:
            word_freq[word_lower] = 1
    # sort word-frequency dictionary
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    # print most frequent words
    print("Most frequent words:")
    for i in range(5):
        print(sorted_word_freq[i][0], ":", sorted_word_freq[i][1])
    # get most frequent letters
    # create letter-frequency dictionary
    letter_freq = dict()
    for letter in a:
        if isalpha(letter):
            letter_lower = letter.lower()
            if letter_lower in letter_freq:
                letter_freq[letter_lower] += 1
            else:
                letter_freq[letter_lower] = 1
    # sort letter-frequency dictionary
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    # print most frequent letters
    print("Most frequent letters:")
    for i in range(5):
        print(sorted_letter_freq[i][0], ":", sorted_letter_freq[i][1])
    average_nb_word_per_line = nb_words / nb_lines
    print("Average number of words per line: {:.2f}".format(average_nb_word_per_line))
