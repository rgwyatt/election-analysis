# election-analysis
## Project Overview
-An employee from the Colorado Board of Elections employee has given me a set of data and included several important pieces of information to be gleaned from the set. That list is as follows:
1. The count of total votes cast
2. A complete list of candidates who did receive votes
3. The total number of votes cast for each candidate
4. The percentage of the total votes each candidate ending up receiving
5. The winner of the election
## Resources
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code 1.50
## Summary
-The election analysis returned the following information, in line with the original requester's tasks:
a. There were 369,711 votes cast.
b. The candidates who received votes were Charles Casper Stockham, Diana DeGette, & Raymon Anthony Doane.
c. The candidate results were:
  i. Charles Casper Stockham recieved 23.0% of the vote with 85,213.
  ii. Diana DeGette received 73.8% of the vote with 272,892.
  iii. Raymon Anthony Doane received 3.1% of the vote with 11,606.
d. The election was won by Dian DeGette with a majority 73.8% of the vote.
## Challenge Overview
The committee member for the Board of Elections came back with additional requested data, pertaining to the following avenues of analysis:
1. The county with the largest voting population
2. The percentage breakdown of votes from each county
3. The county with the highest turnout
## Challenge Results
### How many votes were cast in this congressional election?
There were 369,711 votes cast.
### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
Jefferson county contributed 10.5% of the overall vote with 38,855.
Denver county contributed 82.8% of the overall vote with 306,055.
Arapahoe county conributed 6.7% of the overall vote with 24,801.
### Which county had the largest number of votes?
The largest voting county was Denver county, contributng 306,055 votes at 82.8% of the total vote.
### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Charles Casper Stockham received 23.0% of the total vote with 85,213.
Diana DeGette received 73.8% of the total vote with 272,892.
Raymon Anthony Doane received 3.1% of the total vote with 11,606.
### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Diane DeGette won the election with 272,892 votes, earning 73.8% of the vote.
## Challenge Summary
This script can be applied to future elections as long as the csv document is constructed in the same format. Updating the file that you open with the os.path.join dependency function will be crucial to making sure you're working with the right data set.
You could also apply this same style of script to a wider number of elections variables, as long as they are append in columns 4+. The opening constructions, iterating loops, and print-to-file setups are all formulaic, i.e. "plug and chug". You would just append another section like either the candidates section or the counties section to the opening designations and then the code later down, making sure to mind indents.