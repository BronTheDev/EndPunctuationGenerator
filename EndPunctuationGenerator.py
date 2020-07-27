"""
This simple program takes user input and determines whether the user sentence is a statement or question.
To end program type "end/"
"""


# Function that runs end punctuation generator
def runProgram():
    Paragraph = ""
    while True:
        sentence = input("Say something: ")                     # Ask for user Input

        if sentence == "end/":                                  # Ends program if user inputs "end/"
            break

        Paragraph = Paragraph.__add__(checkSentence(sentence))  # Adds sentence the the paragraph
    print(Paragraph)


# Determines whether or not a period or question mark is needed at the end of a sentence
def checkSentence(sentence):
    isQuestion = False                                            # initializes question variable as False
    interrogativeWords = ["how", "who", "when", "are", "what"]    # List of words that determine whether or not sentence is a question

    # For loop that iterates through list of interrogativeWords
    for word in interrogativeWords:
        if sentence.lower().__contains__(word):                   # Checks if the sentence contains an interrogative word
            isQuestion = True                                     # If sentence contains interrogative word question variable is true
    if isQuestion:
        sentence = sentence.__add__("? ")                         # Adds question mark end of sentence
    else:
        sentence = sentence.__add__(". ")                         # Adds question mark end of sentence
    return sentence.capitalize()                                  # Returns capitalized sentence


runProgram()
