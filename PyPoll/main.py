import os
import csv

# Create variables for calculations
candidates = []   # list of candidate name string
num_votes = 0     # integer keeping track of total number of votes
vote_counts = []  # list of integers tracking individual candidate vote counts

# Get CSV
election_dataCSV = os.path.join('Resources', 'election_data.csv')

# Read CSV
with open(election_dataCSV) as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',')

    # Skip header
    header = next(csvReader,None)

    # Process the data
    for line in csvReader:

        # Add to total number of votes
        num_votes = num_votes + 1

        # Get the name of the candidate for whom the vote was cast
        candidate = line[2]

        # If the candidate has votes>0 add one to the candidate vote total
        # If candidate votes = 0, add the candidate to the candidate list and start
        # counting his or her votes.
        if candidate in candidates:
            vote_counts[candidates.index(candidate)] = vote_counts[candidates.index(candidate)] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)

    # Variables for processed data
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and the winner
    for candidate in range(len(candidates)):
        vote_percentage = vote_counts[candidate]/num_votes*100
        percentages.append(vote_percentage)
    winner = candidates[vote_counts.index(max(vote_counts))]

    # Round decimal
    percentages = [round(i,2) for i in percentages]

    # Print results
    print("\nElection Results")
    print("--------------------------")
    print(f"Total Votes: {num_votes}")
    print("--------------------------")
    for candidate in range(len(candidates)):
        print(f"{candidates[candidate]}: {percentages[candidate]}% ({vote_counts[candidate]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

    #Put results in file
    write_election_dataCSV = f"./analysis/election_analysis.txt"

    # Open write file
    filewriter = open(write_election_dataCSV, mode = 'w')

    # Print to write file
    filewriter.write("Election Results\n")
    filewriter.write("--------------------------\n")
    filewriter.write(f"Total Votes: {num_votes}\n")
    print("--------------------------")
    for candidate in range(len(candidates)):
        filewriter.write(f"{candidates[candidate]}: {percentages[candidate]}% ({vote_counts[candidate]})\n")
    filewriter.write("---------------------------\n")
    filewriter.write(f"Winner: {winner}\n")
    filewriter.write("---------------------------\n")

    # Close file
    filewriter.close()