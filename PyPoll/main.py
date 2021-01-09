import os
import csv

file = os.path.join("Resources","ElectionData.csv")

votes_total = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0


with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        votes_total = votes_total + 1

        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

    for key, value in candidates.items():
        candidates_percent[key] = round(((value/votes_total)*100),3)

    for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]
            

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votes_total}")
    print("-------------------------")
    for key, value in candidates.items():
        print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")


    analysisfile = os.path.join("analysis/analysis.txt")
    
    analysis = open(analysisfile,"w")

    analysis.write("Election Results \n")
    analysis.write("------------------------- \n")
    analysis.write(f"Total Votes: {votes_total} \n")
    analysis.write("------------------------- \n")
    for key, value in candidates.items():
        analysis.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    analysis.write("------------------------- \n")
    analysis.write(f"Winner: {winner} \n")
    analysis.write("------------------------- \n")