import random, string

# Function to mutate a string.
def mutateString(mutant, target):
	# Cut down the string to match target size
	if len(mutant) <> len(target):
		print "[WARN]: Length of mutant and target are different, trimming to continue"
		mutant = mutant[0:len(target)]
	
	# Only mutate the bits that do not match
	for char in range(0, len(mutant)):
		if target[char] <> mutant[char]:
			mutant[char] = random.choice(string.ascii_lowercase)

	# Return the mutant
	return mutant

# Function to score a mutant against the target string.
def scoreMutant(mutant, target):
	# Score is the number of char which match (positionally)
	score = len(filter(lambda x: mutant[x] == target[x], range(0, len(target))))

	return score

# Function to create the initial mutant that eventually evolves into final target
def createAdam(targetLen):
	adam = []

	for x in range(0, targetLen):
		adam.append(random.choice(string.ascii_lowercase))

	return adam

def runSimulation(arg):
	target = [] 	                                        # Define the target string
	map(lambda x: target.append(x), arg.replace(' ',''))
	mutant = createAdam(len(target))			# Create the initial mutation
	generationCounter = 0					# Counts the number of cycles

	# Print starting status
	print "Starting to find target string : " + str(target)
	print "Starting with seed             : " + str(mutant) + "\n"

	while mutant <> target:

		# Mutate the current mutant
		newMutant = mutateString(mutant, target)

		print "Testing for new mutant  : " + str(newMutant) + "(" + str(scoreMutant(newMutant, target))  + ")"

		# Choose between current and newMutant
		if ((scoreMutant(mutant, target)) < (scoreMutant(newMutant, target))):
			mutant = newMutant
			generationCounter = generationCounter + 1
		else:
			generationCounter = generationCounter + 1

	# Print out closing stats
	print "Target mutant reached in " + str(generationCounter) + " generations."

	return generationCounter
