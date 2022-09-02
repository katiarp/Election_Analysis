# Election Analysis

## Project Overview
The goal of thsi project was to assit the Colorado Board of Elections in an election audit of the tabulated results for U.S Congressional precinct in Colorado. I assited an employee with task of reporting the total number of votes for each candidate and the winner of the election based on the popular vote. My job was to generate a vote count report to certify this US congressional race.

The team working on this project decided  to use Python to write the algoriths to be used to confirm  and analyze the election results. One of the advantages of using Python is that it's easier to perform analysis when working with larga data set.Our data source was a CSV file  including the election results, after a brief inspection i observed that data consisted of a number for the ballot ID, a name for counties and candidates respectively.

After we complete the analysis we need to deliver the following information.

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
I used "headers = next(file_reader)" to skip the headers and get an accurate vote count. Since I had 369,711 more rows to check for the number of candidates, and checking data rows to check to have an accurate count of candidates and their names I used a decision statement to go over the candidates name. 

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

From this, I identified only three candidates in the data set  who received votes.

- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane

After that, I calculated each candidate's vote count and  percentage.
Charles Casper Stockham received a total of 85,213 votes which was 23.0% of the total votes. Raymon Anthony Doane received 11,606 votes, only 3.1% of the total votes. And the winner of the election was Diana DeGette who obtained the most votes, 272,892 votes which was 73.8% of the votes.

This is the formula used in Python to calculate the vote percentage.
```
 #calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
```

Seth needs you to save your election audit results to a text file so he can send it to the election commission. 

## Challenge Overview

After the election commission reviewed the results, they asked for supplemental data to complete their audit. They requested the following:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The couuntly with the highest turnout

For this challenge, I analyzed the code I used in the previous report to find out if I could use part of it to provide the additional information requested.  The first thing I did was  to create a list  that was going to hold the counties names ``` county_list = []``` and a dictionary  ``` county_votes={} ``` to hold the counties' total votes. Then I created new variables to hold the voter turnout for each county and percentage of total count and set them to ``` 0 ```.
With are repetition statement a "``` for loop ```," I calculated the counties

```
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote_count= county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_vote_count_percentage = float(county_vote_count)/float(total_votes)*100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_vote_count_percentage:.1f}% ({county_vote_count:,})\n"
        )
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote_count > largest_county_voter_turnout) and (county_vote_count_percentage> largest_county_voter_percentage):
            largest_county_voter_turnout= county_vote_count
            largest_county_turnout_name = county_name
            largest_county_voter_percentage = county_vote_count_percentage

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout_name}\n"
        f"-------------------------\n"
    )
    print(largest_county_turnout_summary)
    txt_file.write(largest_county_turnout_summary)
```





Working from this module’s election_results.csv file, use for loops and conditional statements with membership and logical operators to find the requested results. Then, print the results to the command line and save them to your election_results.txt file.

Finally, you’ll provide a written analysis of the election audit for the election commission, including the new results and a clearly written overview of your methods. As with all written analyses, this will help your audience understand what you did and what they might be able to do with the data you presented.
## Challenge Summary


1.	Overview of Election Audit: Explain the purpose of this election audit analysis.
2.	Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
o	How many votes were cast in this congressional election?
o	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
o	Which county had the largest number of votes?
o	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
o	Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
3.	Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
