#module 3.5.5
import csv
import os

# The data we need to retrieve.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect file path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# open the election results and read the file
with open(file_to_load) as election_data:

    #to do: perform analysis
    file_reader = csv.reader(election_data)
    #Read and prin the header row
    headers = next(file_reader)
    #print(headers)
    #pring each row in the file
    for row in file_reader:
        #2 add to the total vote count
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]
        #add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
           
           #begin tracking the candidates vote
            candidate_votes[candidate_name] = 0
        
        #add a vote to that candidates count
        candidate_votes[candidate_name] += 1


    
    #determine the percentage of votes for each candidate by looping through the counts
    #1. iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. retrive vote count of candidate
        votes = candidate_votes[candidate_name]
        #3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4 print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
        #determine winning vote count and candidate
        #1. determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
            f"-----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------\n")
        print(winning_candidate_summary)

#print the candidates
#print(candidate_options)
#3 print the total votes
#print(total_votes)
#print the candidate vote dictionary
#print(candidate_votes)
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.