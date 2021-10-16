# Election-Analysis-Mod3

Create an Election Analysis "PyPoll" with Python

**Overview of Project**
A Colorado Board of Elections employee has tasked us with completing the election audit of a recent local congressional election. As part of our audit we will be performing the following actions:
1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received votes.
3.	Calculate the total number of votes each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on popular vote.

**Election-Audit Results:**

After our script performed analysis on the raw data we saved under the Resources titled election_results.csv we obtained the following results of our analysis per the image below. This image comes from the election_results.txt file that we created within our Python code.

![image](https://user-images.githubusercontent.com/91284661/137595006-7f1135d6-0310-4540-a93b-4b83dcd11330.png)
 
Election Results Txt File:

![image](https://user-images.githubusercontent.com/91284661/137594993-de0c7734-eb7c-4f32-8bd7-9e1a2491d3ef.png)

**Total Votes Cast** in this congressional election was 369,711

**County Votes:**

•	Jefferson county has 10.5% total percentage with a total vote count of 38,855

•	Denver county has the 82.8% total percentage with a total vote count of 306,055

•	Arapahoe county has 6.7% total percentage with a total vote count of 24,801

**County with Largest Number of Votes:**

•	Denver county has the largest number total of 306,055

•	In addition, Denver county has the total votes percentage of 82.8%

•	Denver county is the Largest County Turnout

**Candidate Percentage of Votes:**

•	Charles Casper Stockham candidate has 23.0% total percentage with total votes: 85,213

•	Diana DeGette candidate has the 73.8 total percentage with total votes: 272,892

•	Raymon Anthony Doane candidate has 3.1% total percentage with total votes: 11,606

**Election Results:**

•	Diana DeGette won the election, with a total votes of 272,892

•	In addition, Diana DeGette has the total percentage votes of 73.8%

•	Diana DeGette is the Winner!

**Election-Audit Summary**

Our code has provided a useful analysis as part of our audit of the election results for this congressional election. Still, it should be observed that with some minor tweaking, our code has uses outside of this election. 

**Ex.1** Since our analysis comes from reviewing the .csv folder titled election_results.csv, if one were to simply capture data for another congressional election within several other counties (i.e. not the three Jefferson, Arapahoe, or Denver that we have), we could effectively run another analysis on another election altogether. If, for example, we had another election using ballot ID data from the county of Boulder, CO (just to name one as part of a larger list) we would obtain the results of our new list. All we would need to change within our code is the file name we are importing our data from as it might not necessarily be titled “election_results.csv” that we used to perform this audit.

![image](https://user-images.githubusercontent.com/91284661/137594987-b24a8445-e9ce-4baf-9b5d-51cdbb56a4f9.png)

**Ex.2** Furthermore, the building blocks of our code also would allow us to perform an audit not necessarily like this congressional election. For example, if we were auditing a presidential election, then provided we had data, then we could end up performing a similar analysis based on the vote counts within precincts instead of counties, which presidential elections within the United States use to declare a winner.
