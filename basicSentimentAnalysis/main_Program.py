#importing Pword and Nword files
from Pword import *
from Nword import *
theTweet = input("enter the sentence")
import re
theTokens = re.findall(r'\b\w[\w-]*\b', theTweet.lower())
#print(theTokens[:5])
numPosWords = 0
for word in theTokens:
    if word in positive_words:
        numPosWords += 1

numNegWords = 0
for word in theTokens:
    if word in negative_words:
        numNegWords += 1

if numPosWords > numNegWords:
    print("   The given sentence is Positive " + str(numPosWords) + ":" + str(numNegWords))
elif numNegWords > numPosWords:
    print("   The given sentence is Negative " + str(numPosWords) + ":" + str(numNegWords))
elif numNegWords == numPosWords:
    print("Neither " + str(numPosWords) + ":" + str(numNegWords))
    
print()
