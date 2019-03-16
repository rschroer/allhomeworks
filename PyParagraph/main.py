import os
import datetime as dt 
import re

input_file=os.path.join("raw_data", "paragraph_3.txt") #input("Please type the filename "))
paragraph_text=""
words=[]

with open(input_file,"r") as paragraph:
    paragraph_text=paragraph.read().replace('\n', ' ')

sentences=re.split("(?<=[.!?]) +", paragraph_text)
words=re.split("(\s+)", paragraph_text)
[word.remove(" ") for word in words]


print(len(sentences))
print(words)