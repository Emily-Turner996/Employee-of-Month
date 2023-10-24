# Set up/initialize necessary variable(s):
fileName = 'october2023.txt' # so i can manually (for now) change the name of the file to be used each month


# Function Definitions:
"""
newVote() - function that allows user to vote
This was originally just going to be the main part of the program without being in a function, but I'm putting it here
because I plan on making additions to the program as a whole and this will make it more organized/easier to work with 
when the time comes. 

Function prompts user for their ID and who they want to vote for, and appends it to the file unless they've already voted.
"""
def newVote():
    userID = input("Please enter the 4-digit pin you use to clock in: ")  # prompt user for their ID

    # checking to see if the voter has voted already
    if checkUserID(userID) == True:
        vote = input("Who do you think should win employee of the month?: ")  # prompt user for their vote
        ballot = (userID + " " + vote + "\n")  # saving information to be appended in a single line for formatting & testing
        votes.write(ballot)  # append the vote to the text file
        print("Vote saved successfully.")

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





# Setting up file for use:
votes = open(fileName, "a+") # open file so that it can be read and appended to
votes.seek(0) # This line helps program to read file correctly, thanks StackOverflow!
ballotArray = votes.readlines() # save contents of text file into an array, split by lines




# Main Program:
newVote() # Function that allows user to vote




# Close File
votes.close()

# Exit Program
exit()