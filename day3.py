f = open("input.txt", "r")

lines = f.read().splitlines()

def bitcriterium(strings, position):
    one, zero = 0, 0
    for i in range(len(strings)):
        if strings[i][position] == "1":
            one += 1
        else: 
            zero += 1
    return [zero, one]

bitcriterium(lines, 0)

def filt(strings, startbit, position):
    output = [x for x in strings if x[position] == startbit]
    return output

def oxystep(strings, criterium, position):
    if criterium[0] > criterium[1]:
        output = filt(strings, startbit = "0", position=position)
    elif criterium[0] <= criterium[1]:
        output = filt(strings, startbit = "1", position=position)
    return output

def scrubberstep(strings, criterium, position):
    if criterium[0] <= criterium[1]:
        output = filt(strings, startbit = "0", position=position)
    elif criterium[0] > criterium[1]:
        output = filt(strings, startbit = "1", position=position)
    return output

def get_ratings(strings):
    oxystrings, scrubberstrings = strings, strings
    output = ["", ""]
    for j in range(len(strings[0])):
        oxycrit = bitcriterium(oxystrings, j)
        oxystrings = oxystep(oxystrings, oxycrit, j)
        scrubbercrit = bitcriterium(scrubberstrings, j)
        scrubberstrings = scrubberstep(scrubberstrings, scrubbercrit, j)
        print(oxycrit, scrubbercrit)
        if len(oxystrings) == 1: 
            output[0] = oxystrings[0]
        if len(scrubberstrings) == 1:
            output[1] = scrubberstrings[0]
    return output
    
ratings = get_ratings(lines)

# decimal values
3443 * 1357
