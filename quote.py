import random,time
#seed the time
#random.seed(time.time())
# cold run
# cold bike
# replace seed with random number range
def getcbquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/cold_quote.txt', "rU" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q1 = quote
    q1 = str(q1).strip('][')
    return q1
# hot bike
def gethbquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/hot_quote.txt', "rU" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q2 = quote
    q2 = str(q2).strip('][')
    return q2
# tri
def gettriquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/tri_quote.txt', "rU" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q4 = quote
    q4 = str(q4).strip('][')
    return q4
# wet bike
def getwbquotes():
    random.seed(time.time())
    quotelist = []
    infile = open( '/Users/paul/Documents/twcHack/quotes/wet_quote.txt', "rU" )
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    q5 = quote
    q5 = str(q5).strip('][')
    return q5

#b = gethbquotes()
#b = str(b)
#b = b.encode('utf-8')
#print 'b'
#print b[1:-1]
#x = getcbquotes()
#print 'x'
#print x
#y = getwbquotes()
#print 'y'
#print y
#z = gettriquotes()
#z = str(z).encode('utf-8')
#print 'z'
#print '%s' %(z)




