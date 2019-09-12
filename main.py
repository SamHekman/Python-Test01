import sys
import re 

# Input str via command line using stdin.
line = str(sys.stdin.readline()) 

# Check if line variable is over the limit of 1,000,000 characters in length
if len(line) > 1000000:
	print("Input string exceeds character limit of 1,000,000")
	sys.exit()

# Check if line variable contains any character that is not a numerical character.
elif not re.match("^[0-9]*$", line):
	print("Input string contains unacceptable character types, all character must be 0-9")
	sys.exit()

def main(line):

	# Build a repository to hold all palindromic substrings discovered.
	result = []

	# Select "chunk" as every possible substring in line str.
	for ending_char in range(len(line)): 
		for starting_char in range(0, ending_char):
			chunk = line[starting_char:ending_char + 1] 


            # Check if every possible substring is a palindrome,
            # by checking the reverse of each substring against itself.
			if chunk == chunk[::-1]: 
				result.append(chunk)

	# Returns longest palindrome using length as the search key.
	return max(result, key = len)

# output string to command line using stdout
sys.stdout.write(main(line))
