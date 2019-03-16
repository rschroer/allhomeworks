import os
import csv
import datetime as dt

in_file=os.path.join(".","election_data.csv")
out_file=os.path.join(".","poll_analysis.txt")

candidates=[]
votes_cast=[]
tally={}
votecounter=[]


#this is for QAing runtime
start_time=dt.datetime.now()

#this function creates the output format



#read in the file
with open(in_file, "r") as votes:
    csv_in=csv.reader(votes)
    ##Skip the header ine
    next(csv_in)
    for ballot in csv_in:
        votes_cast.append(ballot[2])

#calculate the number of total votes
total_votes=len(votes_cast)

#dedup the candidates and create a dictionary with their names as keys
candidates=set(votes_cast)
tally={candidate:0 for candidate in candidates}

#loop through the candidates, count the votes and update the dictionary with their value
for elector in tally.keys():
    votecounter.clear()
    [votecounter.append(vote) for vote in votes_cast if vote==elector]
    tally[elector]=len(votecounter)


sorted_tally=dict(sorted(tally.items(), key=lambda kv: kv[1], reverse=True))
winner=[candidate for candidate, votes in tally.items() if votes==max(tally.values())]


print(f"Election Results")
print(f"-------------------")
for candidate in sorted_tally:
    print(f"{candidate}: {round(sorted_tally[candidate]/total_votes*100,3)} ({sorted_tally[candidate]})")
print(f"-------------------")
print(f"Winner: {winner[0]}")
print(f"-------------------")

#this is for QAing runtime
runtime=(dt.datetime.now()-start_time).total_seconds()
print(runtime)

