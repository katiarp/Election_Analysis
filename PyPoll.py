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

#Assing a variable for the file to load
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save= os.path.join("Analysis","election_analysis.txt")

#Initialize a total vote counter
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
    #Read the file object with the reader funcion.
    file_reader = csv.reader(election_data)
    #Read he header row
    headers= next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
       #Add to the total vote count
        total_votes+=1 
        #Print the candidate name from each row
        candidate_name= row[2]
        #if the candidate doesn't match any existing candidate add the candidate list
        if candidate_name not in candidate_options:
             #Add it to the candidate list.
            candidate_options.append(candidate_name)  
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]= 0
            #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

#Save the results to our text file.
with open(file_to_save,'w') as txt_file:
    #After opening the file print the final vote count to the terminal
    election_results =(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")

    #After printing the final vote count to the terminal save the final vote count to the text file
    txt_file.write(election_results)
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        #variable candidate results candidate name; their voter count, and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")   
        #print each candidate
        print(candidate_results)
        #Save the candidate results to our text file
        txt_file.write(candidate_results)

        #Determine winning vote count winning percentage, and candidate.
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            #if true then set winning_count = votes and winning_percent=
            #vote_percentage
            winning_count= votes
            winning_percentage = vote_percentage
            #And, set the winning_candidate equal to the candidate's name
            winning_candidate=candidate_name
        
    #Print the winning candidates' results to the terminal
    winning_candidate_summary= (
        f"-------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )
    print(winning_candidate_summary)
    #Save the winnin candidate's result to the text file
    txt_file.write(winning_candidate_summary)

