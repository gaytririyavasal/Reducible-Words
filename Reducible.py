#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Reducible.py

#  Description: Finds the largest reducible word from given dictionary

#  Student Name: Gaytri Vasal

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/22/22

#  Date Last Modified: 3/25/22

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    # constant - (key % const)
    step_size = const - hash_word(s, const)
    return step_size

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    # find hash_index
    hash_index = hash_word(s, len(hash_table))
    # find step size, 11 is arbitrary constant
    size = step_size(s, 11)
    # loop through hash_table while the index is not empty
    while hash_table[hash_index] != "":
        hash_index += size
        hash_index %= len(hash_table)
    # if index is empty, add s
    hash_table[hash_index] = s
    

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    # find hash_index
    hash_index = hash_word(s, len(hash_table))
    # if initial index is empty, then s is not in hash_table
    if hash_table[hash_index] == "":
        return False
    # find step size, 11 is arbitrary constant
    size = step_size(s, 11)
    # loop while hash_index of hash_table does not contain s
    while hash_table[hash_index] != s:
        hash_index += size
        hash_index %= len(hash_table)
        # if index is empty, then s is not in hash_table
        if hash_table[hash_index] == "":
            return False
    return True
    
    

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    # base cases
    # checks if word is already in hash_memo
    if find_word(s, hash_memo):
        return True
    # checks if word is a, i, or o
    if (s == "a" or s == "i" or s == "o"):
        return True
    # checks if word is not in hash_table
    if not find_word(s, hash_table):
        return False
    
    # loops through each letter of string
    for char in range(len(s)):
        # removes letter from word
        new_word = s[:char] + s[char + 1:]
        # checks to see if word is reducible
        if is_reducible(new_word, hash_table, hash_memo):
            # insert word if it is
            insert_word(s, hash_memo)
            return True
    return False
   
  


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    longest_words = []
    max_length = 0
    
    # finds the longest length
    for word in string_list:
        if len(word) > max_length:
            max_length = len(word)
    
    # appends all words of max length
    for word in string_list:
        if len(word) == max_length:
            longest_words.append(word)
    
    return longest_words

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  n = 2*length + 1
  while (not is_prime(n)):
      n += 1
      

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(n):
      hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
      insert_word(word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  m = int(0.2*length + 1)
  while (not is_prime(m)):
      m += 1

  # populate the hash_memo with M blank strings
  for i in range(m):
      hash_memo.append("")

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
      if is_reducible(word, hash_list, hash_memo):
          reducible_words.append(word)

  # find the largest reducible words in reducible_words
  largest = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  largest = sorted(largest)
  for word in largest:
      print(word)
  

if __name__ == "__main__":
  main()
