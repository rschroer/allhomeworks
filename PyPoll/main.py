import os
import csv
import datetime as dt

#file settings
in_file=os.path.join(".","election_data.csv")
out_file=os.path.join(".","poll_analysis.txt")

#initial declaration
candidates=[]
votes_cast=[]
tally={}
votecounter=[]

#this is for QAing runtime
#start_time=dt.datetime.now()

#this function creates the output format
def format_output(voting_dictionary):
    #calculate the winner
    winner=[candidate for candidate, votes in tally.items() if votes==max(tally.values())]
    #this loops gerneates the results display
    format_helper=""
    for candidate in voting_dictionary:
        format_helper+=f"{candidate}: {round(sorted_tally[candidate]/total_votes*100,3)} ({sorted_tally[candidate]})\n"
    output_string= (f"Election Results\n"
                    f"-------------------\n"
                    f"{format_helper}"
                    f"-------------------\n"
                    f"Winner: {winner[0]}\n"
                    f"-------------------")
    return output_string


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

#sort the vote tally
sorted_tally=dict(sorted(tally.items(), key=lambda kv: kv[1], reverse=True))

#format the output after realizing that I asigned this to a variable, 
# I don't think I needed to make a function and it would be faster without one
formatted_output=format_output(sorted_tally)

#write to std out
print(formatted_output)

#Write to file
with open(out_file, "w" ) as output:
    output.write(f"{formatted_output}")

#this is for QAing runtime
#runtime=(dt.datetime.now()-start_time).total_seconds()
#print(runtime)

