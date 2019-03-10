import os
import csv

in_file=os.path.join(".","election_data.csv")
out_file=os.path.join(".","poll_analysis.txt")

candidates=[]
votes_cast=[]
weirdostuff=[]

with open(in_file, "r") as votes:
    csv_in=csv.reader(votes)
    ##Skip the header ine
    next(csv_in)
    for ballot in csv_in:
        votes_cast.append(ballot[2])

total_votes=len(votes_cast)
candidates=set(votes_cast)
[weirdostuff.append(vote) for vote in votes_cast if vote=='Khan']
print(len(candidates))
print(candidates)