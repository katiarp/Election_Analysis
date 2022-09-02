# Election Analysis

## Project Overview
The goal of this project was to help the Colorado Board of Elections in an election audit of the tabulated results for U.S Congressional precinct in Colorado. I assisted an employee with the task of reporting the total number of votes for each candidate and the winner of the election based on the popular vote. My job was to generate a vote count report to certify this US congressional race.

The team working on this project decided  to use Python to write the algorithms  to confirm  and analyze the election results. One of the advantages of using Python is that it's easier to perform analysis when working with large data sets. Our data source was a CSV file  including the election results; after a brief inspection, I observed that data consisted of a number for the ballot ID, a name for counties and candidates.

After we complete the analysis, we need to deliver the following information.

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

### Resources 
- Data Source: election_results.csv
- Software: Python 3.9.12
- Visual Studio Code 1.70.2

## Summary
The analysis showed that 369,711 votes were cast in the election. To find the total number of votes I used the following code script.

```
headers= next(file_reader)
    for row in file_reader:
       #Add to the total vote count
        total_votes+=1
 ```
I used "headers = next(file_reader)" to skip the headers to get an accurate vote count. Since I had 369,711 rows to check for the number of candidates, I used a decision statement to go over the candidates name to have an accurate count of candidates

```
candidate_name= row[2]
        if candidate_name not in candidate_options:
             #Add candidate to list
            candidate_options.append(candidate_name)  
            #Tracking candidate's vote count.
            candidate_votes[candidate_name]= 0
            #Add a vote to candidate's count
        candidate_votes[candidate_name] +=1
```

From this, I identified only three candidates in the data set.

- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane

After that, I calculated each candidate's vote count and percentage.
Charles Casper Stockham received a total of 85,213 votes which was 23.0% of the total votes. Raymon Anthony Doane received 11,606 votes, only 3.1% of the total votes. And the winner of the election was Diana DeGette who obtained the most votes, 272,892 votes which was 73.8% of the votes.

This is the formula used in Python to calculate the vote percentage.
```
 #calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
```

 

## Challenge Overview

After the election commission reviewed the results, they asked for supplemental data to complete their audit. They requested the following:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

For this challenge, I analyzed the code I used in the previous report to find out if I could use part of it to provide the additional information requested. 

## Challenge Summary

 The first thing I did was  to create a list  that was going to hold the counties names ``` county_list = []``` and a dictionary  ``` county_votes={} ``` to hold the counties' total votes. Then I created new variables to hold the voter turnout for each county and percentage of total count and set them to ``` 0 ```.
With are repetition statement, a ``` for loop ```, I calculated the voter turnout for each county and their percentage of votes out of the total count. Using a decision statement I identified the county with the highest voter turnout. The county with the largest turnout was **Denver**

```
    # Get the county from the county dictionary.
    for county_name in county_votes:
        # Retrieve the county vote count.
        county_vote_count= county_votes.get(county_name)
        # Calculate the percentage of votes for the county.
        county_vote_count_percentage = float(county_vote_count)/float(total_votes)*100

         # Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_vote_count_percentage:.1f}% ({county_vote_count:,})\n"
        )
        print(county_results)
         # Save the county votes to a text file.
        txt_file.write(county_results)

         # Determine the winning county and get its vote count.
        if (county_vote_count > largest_county_voter_turnout) and (county_vote_count_percentage> largest_county_voter_percentage):
            largest_county_voter_turnout= county_vote_count
            largest_county_turnout_name = county_name
            largest_county_voter_percentage = county_vote_count_percentage

    largest_county_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout_name}\n"
        f"-------------------------\n"
    )
    print(largest_county_turnout_summary)
    txt_file.write(largest_county_turnout_summary)
```

Finally, within the code I saved each result to an output text file called **election_analysis.txt**. This text file will be useful for the election  commission because they can use it to review  the findings or share it with other stakeholders.


![Image_name](/Resources/election_analysis_image.png)

## Summary Statement

This script can be modified to process the election results of any other election. 
Currently, the script can only work with .csv election data files, and the delimiter must be “,” and all the election data files must have the following header row columns, in order:

![Image_name](/Resources/election_results_csv_image.png)

Therefore we will need to make sure that the file to be processed meets the above criteria; otherwise, we must modify the script in order to process other types of file.

Some ways in which we could modify the script to be used for any other election are the following:
1. In variable file_to_load, we could replace the current path of the election data file with the path of the   new data file to be processed.

2. In variable file_to_save, replace the current election results file path with the new file path to save the election results in. 

Overall, we could modify our script adding different variables to make further analysis, furthermore we could use a descriptive name to identify the file in the future, e.g “California 2022 election results.txt”
