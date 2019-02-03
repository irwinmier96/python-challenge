import os

import csv

csvpath = os.path.join('election_data.csv')

Khan_vote = []
Correy_vote = []
Li_vote = []
O_Tooley_vote = []

Winner = {}

with open(csvpath, newline = '') as csvfile:

    csvreader =csv.reader(csvfile, delimiter = ',')

    for total_votes in csvreader:

        total_votes = csvreader.line_num - 1

    print(f"Total Votes: {total_votes}")

    csvfile.seek(0)
    next(csvreader)

    for votes in csvreader:
        if votes[2] == "Khan":
            Khan_vote.append(votes[2])
            Khan_percent = (len(Khan_vote)/total_votes) * 100
        elif votes[2] =="Correy":
            Correy_vote.append(votes[2])
            Correy_percent = (len(Correy_vote)/total_votes) * 100
        elif votes[2] == "Li":
            Li_vote.append(votes[2])
            Li_percent = (len(Li_vote)/total_votes) * 100
        elif votes[2] == "O'Tooley":
            O_Tooley_vote.append(votes[2])
            O_Tooley_percent = (len(O_Tooley_vote)/ total_votes) * 100

    Winner["Khan"] = len(Khan_vote)
    Winner["Correy"] = len(Correy_vote)
    Winner["Li"] = len(Li_vote)
    Winner["O'Tooley"] = len(O_Tooley_vote)
    candidates = list(Winner.keys())
    vote_count = list(Winner.values())
    candidate_votes = candidates[vote_count.index(max(vote_count))]
    print(Winner)

    print(f"Khan: {round(Khan_percent, 3)}%  ({len(Khan_vote)})")
    print(f"Correy: {round(Correy_percent, 3)}%  ({len(Correy_vote)})")
    print(f"Li: {round(Li_percent, 3)}%  ({len(Li_vote)})")
    print(f"O'Tooley: {round(O_Tooley_percent, 3)}%  ({len(O_Tooley_vote)})")
    print(f"Winner: {candidate_votes}")