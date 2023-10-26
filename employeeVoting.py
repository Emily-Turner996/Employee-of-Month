# Set up/initialize necessary variable(s):
fileName = 'october2023.txt' # so i can manually (for now) change the name of the file to be used each month


# Function Definitions:
"""
newVote() - function that allows user to vote
This was originally just going to be the main part of the program without being in a function, but I'm putting it here
because I plan on making additions to the program as a whole and this will make it more organized/easier to work with 
when the time comes. 

Function prompts user for their ID and who they want to vote for, and appends it to the file unless they've already voted.

Function takes ballotArray because that array must be updated when new votes come in for the accuracy of other functions
"""
def newVote(ballotArray):
    userID = input("Please enter the 4-digit pin you use to clock in: ")  # prompt user for their ID

    # checking to see if the voter has voted already
    if checkUserID(userID) == True:
        vote = input("Who do you think should win employee of the month?: ")  # prompt user for their vote
        confirmVote(vote) #TEST FOR THE MINUTE
        ballot = (userID + " " + vote + "\n")  # saving information to be appended in a single line for formatting & testing
        votes.write(ballot)  # append the vote to the text file
        ballotArray.append([userID, vote]) # need to update ballotArray here so that the correct number of votes can be counted
        print("Vote for " + vote + " saved successfully.")

    elif checkUserID(userID) == False:
        print("You've already voted.")

    else:
        print("Sorry, there seems to be a program error. Try again later.")  # just a backup in case something goes wrong


""" 
checkUserID(userID) - Function to check if the user has voted already.
The function checks the userID against all the other userIDs in the text file. It assumes it doesn't appear already (True)
until proven otherwise (False). 
Function returns the boolean indicating if they've voted already or not. 
"""
def checkUserID(userID):
    newID = True # assuming the user hasn't voted until proven otherwise
    for i in range(len(ballotArray)): #looping through the array from file
        ballotEntry = ballotArray[i].split() #looking at a single line from the file
        ballotID = ballotEntry[0] #focusing on the userID

        # comparison:
        if userID == ballotID:
            newID = False # make appropriate changes since a match has been found

    return newID # return the correct boolean


"""
Function to make sure the user didn't make a mistake when typing who they voted for. This function exists to help with potential user error.
"""
def confirmVote(vote):
    confirmedVote = vote
    confirmation = input("Are you sure you want to vote for " + confirmedVote + "? [y/n]: ").lower().strip() #get input and format it to be lowercase and remove (external) whitespace

    while(confirmation != 'y'): #loop runs until user enters 'y'
        if (confirmation == 'n'): # if the user enters 'n', code runs to get their new vote
            confirmedVote = input("Enter the name of the person you'd like to vote for: ")
        else: # if the user entered neither y or n, prompt them to only enter y or n
            print("Please only enter 'y' or 'n'")

        confirmation = input("Are you sure you want to vote for " + confirmedVote + "? [y/n]: ").lower().strip() #make sure this is actually the person they want to vote for before it gets saved




"""
numBallots(ballotArray) - Function to calculate and display the number of people who have voted.
"""
def numBallots(ballotArray):
    ballotCount = str(len(ballotArray)) # calculate the number of votes
    print("Total number of votes saved: " + ballotCount) # display results


# Setting up file for use:
votes = open(fileName, "a+") # open file so that it can be read and appended to
votes.seek(0) # This line helps program to read file correctly, thanks StackOverflow!
ballotArray = votes.readlines() # save contents of text file into an array, split by lines




# Main Program:
newVote(ballotArray) # Function that allows user to vote
numBallots(ballotArray) # Function that calculated and display the number of votes so far



# Close File
votes.close()

# Exit Program
exit()