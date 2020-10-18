# SETUP
## Add our dependencies.
import csv
import os

## Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

## Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#ESTABLISH VARIABLES
## Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        ###print(row)
# DATA IN NEED OF RETRIEVAL
## Total num of votes cast
        total_votes += 1

## Complete list of candidates who were voted for
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
    #print(candidate_options)

## Num votes per each candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    #print(total_votes)
    #print(candidate_votes)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

## % of votes each candidate won
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (votes / total_votes) * 100
        #print(f"{candidate_name}: received {round(vote_percentage, 2)}% of the vote.")

## Election winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

# OUTPUT THE DATA
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)  
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
## Create a filename variable to a direct or indirect path to the file. || file_to_save = os.path.join("analysis", "election_analysis.txt")
## Using the with statement open the file as a text file. || with open(file_to_save, "w") as txt_file: ||    ## Write some data to the file. ||    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# Close the file source || ### election_data.close()