import random

def coinToss(numAttempt):
	totalHeads = 0
	totalTails = 0
	for number in range(1,numAttempt+1):
		randomNum = round(random.random())
		print str(randomNum)

		#1 is heads
		if (randomNum == 1):
			totalHeads = totalHeads + 1
			print "Attempt #" + str(number) + " throwing a coin... It's a head!...Got " + str(totalHeads) + " head(s) so far and " + str(totalTails) + " tali(s) so far"
		else:
			totalTails = totalTails + 1
			print "Attempt #" + str(number) + " throwing a coin... It's a tail!...Got " + str(totalHeads) + " head(s) so far and " + str(totalTails) + " tali(s) so far"			

print "Enter number of tries to toss a coin:"
coinToss(input())