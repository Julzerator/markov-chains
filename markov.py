import sys


def make_chains(corpus):
    """Takes input list of strings; returns dictionary of markov chains."""
    c_dict = {}

    for x in range(len(corpus)):
        if x < (len(corpus)-2): # not in edge
            bigram_tuple = tuple([corpus[x],corpus[x+1]])
            if bigram_tuple in c_dict:
                c_dict[bigram_tuple].append(corpus[x+2])
            else:
                c_dict[bigram_tuple] = [corpus[x+2]]

    return c_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

filename = sys.argv[1]

# Make a list of all the words as a string in the .txt file
input_text = open(filename).read().strip("\n").split()



# Get a Markov chain
chain_dict = make_chains(input_text)


# Produce random text
random_text = make_text(chain_dict)

print random_text
