#!/bin/python3

import re


def stemmer(text):
  """
  Stems a given text by removing suffixes "ed", "ly", and "ing".

  Args:
      text: The input text string.

  Returns:
      A string with the suffixes removed from each word.
  """

  if not isinstance(text, str):
    raise ValueError("Input text must be a string.")

  words = text.split()
  stemmed_words = []
  suffixes = ["ed", "ly", "ing"]
  for word in words:
    for suffix in suffixes:
      if word.endswith(suffix):
        stemmed_word = word[:-len(suffix)]
        stemmed_words.append(stemmed_word)
        break  # Only remove the first matching suffix
    else:
      stemmed_words.append(word)  # Append word if no suffix removed
  return " ".join(stemmed_words)


if __name__ == '__main__':
  try:
    text = input("Enter text to stem: ")
    result = stemmer(text)
    print("Stemmed text:", result)
  except ValueError as e:
    print("Error:", e)
