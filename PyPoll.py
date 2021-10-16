# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

#1: Create county list and county vote dictionary
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_county = 0
winning_percentage = 0
winning_c_percentage = 0

#2: Track the largest county and county voter turnout
lrg_county_turnout = ""
lrg_county_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        #3: Pull county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #4a If county does not match any existing county:
        if county_name not in county_options:

            #4b: Add extiting county to list
            county_options.append(county_name)

            #4c: Initializes the county vote to zero aka track county vote count
            county_votes[county_name] = 0

        #5 Add vote to county vote count
        county_votes[county_name] += 1


# Save the results to our text file.
with open("election_results.txt", "w") as txt_file:

    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    #6a Write a repetition statement to get the county from the county dictionary from Step 1
    for county_name in county_votes:

        #6b Retrieve county votes within dictionary
        county = county_votes.get(county_name)

        #6c Calculate county’s votes as a percentage of the total votes
        county_percentage = float(county) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({county:,})\n")
        
        #6d Print current county, results
        print(county_results, end="")

        #6e This step will be completed in Deliverable 2.
        txt_file.write(county_results)

        #6f Decision statement that determines county winning county, vote count
        if (county > winning_county) and (county_percentage > winning_c_percentage):
            winning_county = county
            winning_c_candidate = county_name
            winning_c_percentage = county_percentage

    #7 Write a print statement that prints out the county with the largest turnout
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_c_candidate}\n"
        f"---------------------------\n")
    print(winning_county_summary)

    #8 Save county with largest vote count to text file
    txt_file.write(winning_county_summary)

     # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
