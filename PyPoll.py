#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election

# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.


#import dependencies
import csv
import os
from tkinter import N

#Assing a variable for the file to load
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path.
file_to_save= os.path.join("Analysis","election_analysis.txt")

#1.Initialize a total vote counter
total_votes=0
#Candidate Options
candidate_options=[]
#Declare empty candidate dictionaries
candidate_votes ={}
#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    # #To do: read and analyze the data here
    #Read the file object with the reader funcion.
    file_reader = csv.reader(election_data)

    #Read he header row
    headers= next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
       #2.Add to the total vote count
        total_votes+=1 
    #Print the candidate name from each row
        candidate_name= row[2]
        #if the candidate doesn't match any existing candidate
        if candidate_name not in candidate_options:
             #Add it to the candidate list.
            candidate_options.append(candidate_name)  
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]= 0
            #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1
    #Determine the percentage of votes for each candidate by looping through the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        #print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    
    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal

        #Determine if the votes is greater than the winning count.
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            #if true then set winning_count = votes and winning_percent=
            #vote_percentage
            winning_count= votes
            winning_percentage = vote_percentage
            #And, set the winning_candidate equal to the candidate's name
            winning_candidate=candidate_name
        #To do: print out the winning candidate, vote count and percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")       

    winning_candidate_summary= (
        f"-------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n"
    )
    print(winning_candidate_summary)
   
