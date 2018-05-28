#PyParagraph Script
#Import modules
import os
import re

#Request path and filename of data file
filepath = input('Please enter path and filename of data file (e.g. "datafolder/datafile.txt"): ')

#Declare and initialize variables to store data
sentences = []
words = []
letter_counts = []

#Open Text file and perform operations
with open(filepath, newline="") as text:
    paragraphs = text.read()
    
    #Split text into sentences
    sentences = re.split('[\.\?\!]\W+', paragraphs)
    
    #Split text into words
    words = re.split('[\.\?\!\W]+', paragraphs)
    words.remove('')                                           #Remove null element at end of list created by regex

#Count number of sentences in text
total_sentences = len(sentences)

#Count number of words in text
total_words = len(words)

#Count number of letters in each word
letter_counts = [len(word) for word in words]

#Count total number of letters
total_letters = 0

for letter_count in letter_counts:
    total_letters = total_letters + letter_count

#Create Text Summary
text_summary = [f'',
                f'Paragraph Analysis',
                f'-----------------------------------',
                f'Approximate Word Count: {total_words}',
                f'Approximate Sentence Count: {total_sentences}',
                f'Average Letter Count: {round(total_letters/total_words, 2)}',
                f'Average Sentence Length: {round(total_words/total_sentences, 2)}',
                f''
               ]

#Print Text Summary in terminal
for item in text_summary:
    print(item)

#Request filename for text file
outputfile = input('Please type filename of new report file (e.g. "text_summary.txt"): ')

#Write Text Summary to text file
with open(outputfile, 'w', newline = "") as report:
    
    for item in text_summary:
        report.write(item + "\r")

