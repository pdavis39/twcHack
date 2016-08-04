import random,time
#seed the time
#random.seed(time.time())
# cold run
# cold bike
# replace seed with random number range
def getcbquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/cold_quote.txt', "rb" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q1 = (quote)#the quote
    #a1 = "\t --"+(quote[1])#the author
    return q1
# hot bike
def gethbquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/hot_quote.txt', "rb" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q2 = (quote)#the quote
    #a2 = "\t --"+(quote[1])#the author
    return q2
# hot run
# tri
def gettriquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/tri_quote.txt', "rb" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q4 = (quote)#the quote
    a4 = "\t --"+(quote[1])#the author
    return q4
# wet bike
def getwbquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/wet_quote.txt', "rb" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q5 = (quote)#the quote
    a5 = "\t --"+(quote[1])#the author
    return q5
# wet run


