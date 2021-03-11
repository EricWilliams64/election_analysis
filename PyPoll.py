#module 3.4.3
import csv
import os

# The data we need to retrieve.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect file path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file
outfile = open(file_to_save, "w")
# write some data to the file
outfile.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
outfile.close()

# open the election results and read the file
with open(file_to_load) as election_data:

    #to do: perform analysis
    file_reader = csv.reader(election_data)
    #Read and prin the header row
    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.