# Import dependencies
import os
import csv

#Path to collect data from the Resouces folder
election_csv = os.path.join("..", "Resources", "election_data.csv")


# Open and read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

     # Read the header row first
    csvheader = next(csvreader)

    #print(f"Header: {csvheader}")
    
    # Define PyPoll's variables
    total_votes = 0
    candidatename_votes = {}
    winner_count = 0
    percentage_votes = {}

     # Read through each row of data after the header
    for row in csvreader:

        # The total number of votes cast
        total_votes = total_votes + 1 

        # A complete list of candidates who received votes and 
        # The total number of votes each candidate won
        if row[2] in candidatename_votes:
            candidatename_votes[row[2]] += 1
        else:
            candidatename_votes[row[2]] = 1
            
        # The percentage of votes each candidate won
        for key, value in candidatename_votes.items():
            percentage_votes[key] =round((value/total_votes)* 100 , 3)
        
        # The winner of the election based on popular vote.
            if percentage_votes[key] > winner_count:
                winner_count = candidatename_votes[key]
                winner = key
    
# print the result on terminal    
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for key, velue in candidatename_votes.items():
    print(key,':' , str(percentage_votes[key]),'%','  ','(',candidatename_votes[key],')')
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# open the output file and write the result to the csv
election_file = os.path.join("..", "Output", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write(f"Election Results\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for key, velue in candidatename_votes.items():
        outfile.write(f"{key}: {str(percentage_votes[key])}%   ({candidatename_votes[key]})\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write(f"-------------------------\n")
  

