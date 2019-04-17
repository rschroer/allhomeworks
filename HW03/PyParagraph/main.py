import os
import re

#user enters the file name
input_file=os.path.join("raw_data", input("Please type the filename in the raw data folder: "))
#initial variables
paragraph_text=""
words=[]

#read file
with open(input_file,"r") as paragraph:
    paragraph_text=paragraph.read().replace('\n', ' ')

#split into sentences, words and letters
sentences=re.split("(?<=[.!?]) +", paragraph_text)
words=re.split(r"\s+", paragraph_text)
letters=len(paragraph_text)

#this counts the words and prints them out
print(f"Paragraph Analysis")
print(f"-----------------")
print(f"Approximate Word Count: {len(words)}")
print(f"Approximate Sentence Count: {len(sentences)}")
print(f"Average Letter Count: {format(letters/len(words),'.2f')}")
print(f"Average Sentence Length: {format(len(words)/len(sentences),'.2f')}")