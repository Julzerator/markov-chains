import sys, random


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
        else:
            bigram_tuple = tuple([corpus[-2],corpus[-1]]) # ran twice. Why?
            c_dict.setdefault(bigram_tuple) # could set a default word? Empty list?

    return c_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    key = random.choice(chains.keys())
    return_string = key[0] + " " + key[1]

    while chains[key] != None: #chains.get(key[-1]) != None: # or len(return_string) =< 140
        next_word = random.choice(chains[key])
        if len(return_string + " " + next_word) > 140:
            break
        return_string = return_string + " " + next_word
        key = (key[1],next_word)

    return return_string


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

# print chain_dict
print random_text
