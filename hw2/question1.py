# Ozan Yetkin | 1908227
# Write a recursive function that generates a list of all anagrams of a given string.

def anagrams_of(s):
	# Define the base case which is basically an empty string
    if len(s) == 1:
        return [s]
    else:
        return anagrams_of(s[1:]) + anagrams_of(s[0])

# Test should return the list of all anagrams
print(anagrams_of("pots"))