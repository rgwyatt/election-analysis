# SETUP
## Add our dependencies.
import csv
import os

## Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

## Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
# DATA IN NEED OF RETRIEVAL
## Total num of votes cast


## Complete list of candidates who were voted for


## Num votes per each candidate


## % of votes each candidate won


## Election winner


# OUTPUT THE DATA
## Create a filename variable to a direct or indirect path to the file. || file_to_save = os.path.join("analysis", "election_analysis.txt")

## Using the with statement open the file as a text file. || with open(file_to_save, "w") as txt_file: ||    ## Write some data to the file. ||    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Close the file source || ### election_data.close()