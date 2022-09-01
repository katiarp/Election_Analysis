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

# #Open the election results and read the file.
with open(file_to_load) as election_data:
    # #To do: read and analyze the data here
    #Read the file object with the reader funcion.
    file_reader = csv.reader(election_data)

    #Read and print the header row
    #############why print to skip?
    headers= next(file_reader)
    print(headers)

