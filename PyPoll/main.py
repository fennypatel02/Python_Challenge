# import packages to read/write CSV files and create dynamic paths to the I/O files
import csv
import os

# define function to fix percentage format to 3 decimal points
# googled the command for the decimal point 
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num


    # create empty lists and variables for storing values and calculations from data
UniqueCandidates = []
VoteCounts = []
VotePercent = []
TotalVotes = 0
WinnerCount = 0

 #Set path for file
election_data = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("Analysis" , "pypoll.txt")

# read the CSV file
with open(election_data, 'r') as electiondata:
    csv_reader = csv.reader(electiondata, delimiter=",")

    # store header rows into a Headers list
    Headers = next(csv_reader)
    
    # for loop to go through each row in the CSV file and count the total number of votes
    
    for row in csv_reader:
            TotalVotes += 1
    
    # get unique candidate names and individual vote counts
            if row[2] not in UniqueCandidates:

            #append the name to UniqueCandidates and a value of 1 to VoteCounts list
                UniqueCandidates.append(row[2])
                VoteCounts.append(1)

            else:

            # get the index of the candidate from the UniqueCandidates list in order to increase the vote count by 1
                CandidateIndex = UniqueCandidates.index(row[2])
                VoteCounts[CandidateIndex] += 1


    # --- calculate percentage of votes for each candidate ---
    for i in range(len(VoteCounts)):
        VotePercent.append(VoteCounts[i] / TotalVotes)

    # --- calculate the winner based on most votes ---
    for i in range(len(VoteCounts)):

        # if the number of votes is greater than WinnerCount (initially zero)
        if VoteCounts[i] > WinnerCount:
            
            #update WinnerCount to the number of votes at index i
            WinnerCount = VoteCounts[i]

            #update Winner to the candidate name at index i
            Winner = UniqueCandidates[i]


output_one = (f" Election Results \n --------------------------------- \n Total Votes: {TotalVotes} " + "\n ---------------------------------  ")
print(output_one)

    

for i in range(len(UniqueCandidates)):
        output_two = (f" \n{UniqueCandidates[i]}: {fixPercent(VotePercent[i])} ({VoteCounts[i]})")
        print( output_two)
       


output_three = (f" --------------------------------- \n Winner : {Winner}  \n ---------------------------------" )
print(output_three)


with open(outputfile , "w") as file:
    file.write = output_one
    file.write = output_two
    file.write = output_three
    


#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------



