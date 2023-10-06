# Code inspired from https://github.com/cantugabriela/Python-Challenge/blob/master/PyPoll/main.py

# PyPoll Analysis 
import os
import csv

# Log file address in py_poll_csv
py_poll_csv = os.path.join('Resources','election_data.csv')

# Define variables
total_votes = 0
candidate_votes = {}
winning_count = 0
# Scan CSV file
with open(py_poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvreader)

    #Loop through the file
    for row in csvreader:
        #Count number of total votes
        total_votes += 1

        #Getting unique candidates names
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        #Counting the votes for each candidate
        candidate_votes[candidate_name] += 1

#Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
winner = ""
winner_votes = 0
for candidate_name, votes in candidate_votes.items():
    percentage = round(votes/total_votes*100, 3)
    print(f"{candidate_name}: {percentage}% ({votes})")
    if votes > winner_votes:
        winner = candidate_name
        winner_votes = votes
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Code inspired from instructor
# Output file
file_to_output = os.path.join("Analysis.txt")

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    # Determine the winner by looping through the counts
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)