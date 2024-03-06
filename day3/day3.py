import logging
import re

logging.getLogger().setLevel(logging.INFO)

#regex for checking special char
regex = re.compile('[&=/$@%#*+-]')

f = open("input.txt")
lines = f.readlines()

#get height and width of engine
height = len(lines)
width = len(lines[0][:-1])
logging.info("Height: %d | Width: %d" % (height, width))

#create engine matrix
engine_matrix = [[0 for x in range(width)] for y in range(height)]

for line_idx in range(height):
    for char_idx in range(width):
        engine_matrix[line_idx][char_idx] = lines[line_idx][char_idx]

engine_matrix_print = '\n'.join(['\t'.join([str(cell) for cell in row]) for row in engine_matrix])

#function to check if number is to be added to running total
def check(line_idx, num_idx, length):
    #search right beside number
    if num_idx > length-1:
        if regex.search(engine_matrix[line_idx][num_idx-length]) != None:
            return True
    if num_idx < width-1:
        if regex.search(engine_matrix[line_idx][num_idx+1]) != None:
            return True
    
    #search above and below rows
    for i in range(length+2):
        if num_idx+1-i > width-1 or num_idx+1-i < length-1:
            continue
        #above row if contains symbol from num_idx-length to num_idx+1
        if line_idx > 0:
            if regex.search(engine_matrix[line_idx-1][num_idx+1-i]) != None:
                return True
        #below row if contains symbol from num_idx-length to num_idx+1
        if line_idx < height-1:
            if regex.search(engine_matrix[line_idx+1][num_idx+1-i]) != None:
                return True
    #base case
    return False

#main program
total = 0
gears = {}

#process line and put numbers in number matrix
numbers = [[0 for x in range(width)] for y in range(height)]
for line_idx in range(height):
    cur_number = ""
    num_len = 0
    for char_idx in range(width):
        cur = engine_matrix[line_idx][char_idx]
        #if cur is symbol, continue loop
        if (regex.search(cur) != None or cur == '.'):
            logging.debug("Cur char is symbol, continuing...")
            continue
        #if next char is a digit
        elif char_idx == width-1 or not(engine_matrix[line_idx][char_idx+1].isdigit()):
            cur_number += cur
            num_len += 1
            logging.info("Number parsed: %s" % cur_number)
            #add number to numbers matrix
            for i in range(num_len):
                numbers[line_idx][char_idx-i] = int(cur_number)
            #check if number should be added
            if check(line_idx=line_idx, num_idx=char_idx, length=num_len):
                logging.info("Number fits criteria, adding to total")
                total += int(cur_number)
            #reset cur_number and num_len
            cur_number = ""
            num_len = 0
            logging.info("Running total: %d" % total)
        else:
            #keep parsing number
            cur_number += cur
            num_len += 1
            logging.debug("Next char is digit, continuing...")
            

print("Total: %d" % total)
print("===============================================\n\n\n\n")

print("Numbers matrix:\n"+str(numbers))
#helper to add to dict
def addtodict(dict, key, val):
    if key in dict:
        dict[key].append(val)
    else:
        dict[key] = [val]

#process gears
for line_idx in range(height):
    for char_idx in range(width):
        cur = engine_matrix[line_idx][char_idx]
        if (cur == "*"):
            logging.debug("Reached * char, checking for gear")
            #perform gear functions
            #if after char 0
            if char_idx > 0:
                logging.debug("char_idx > 0")
                logging.debug("Checking (%d, %d)" % (line_idx, char_idx-1))
                if numbers[line_idx][char_idx-1] > 0:
                    logging.debug("Number exists: %d | Adding to gears" % numbers[line_idx][char_idx-1])
                    addtodict(gears, (line_idx, char_idx), numbers[line_idx][char_idx-1])
            #if before last char
            if char_idx < width-1:
                logging.debug("char_idx < width-1")
                logging.debug("Checking (%d, %d)" % (line_idx, char_idx+1))
                if numbers[line_idx][char_idx+1] > 0:
                    logging.debug("Number exists: %d | Adding to gears" % numbers[line_idx][char_idx+1])
                    addtodict(gears, (line_idx, char_idx), numbers[line_idx][char_idx+1])

            #for lines before and after
            #if line after line 0
            if line_idx > 0:
                prev_was_no = False
                logging.debug("line_idx > 0")
                for i in range(3):
                    if char_idx+1-i >= 0 and char_idx+1-i <= width-1:
                        logging.debug("Checking (%d, %d)" % (line_idx-1, char_idx+1-i))
                        if numbers[line_idx-1][char_idx+1-i] > 0 and not prev_was_no:
                            logging.debug("Number exists: %d | Adding to gears" % numbers[line_idx-1][char_idx+1-i])
                            addtodict(gears, (line_idx, char_idx), numbers[line_idx-1][char_idx+1-i])
                            prev_was_no = True
                        if numbers[line_idx-1][char_idx+1-i] == 0 and prev_was_no:
                            prev_was_no = False
            #if line before last line
            if line_idx < height-1:
                prev_was_no = False
                logging.debug("line_idx < height-1")
                for i in range(3):
                    if char_idx+1-i >= 0 and char_idx+1-i <= width-1:
                        logging.debug("Checking (%d, %d)" % (line_idx+1, char_idx+1-i))
                        if numbers[line_idx+1][char_idx+1-i] > 0 and not prev_was_no:
                            logging.debug("Number exists: %d | Adding to gears" % numbers[line_idx+1][char_idx+1-i])
                            addtodict(gears, (line_idx, char_idx), numbers[line_idx+1][char_idx+1-i])
                            prev_was_no = True
                        if numbers[line_idx+1][char_idx+1-i] == 0 and prev_was_no:
                            prev_was_no = False

logging.info("Gear dict: "+str(gears))

#multiplying all values of a list
def mult(lst):
    total = 1
    for item in lst:
        total *= item
    return total

#calculate gear total
gear_total = 0
for key, val in gears.items():
    if len(val) == 2:
        logging.debug("Gear "+str(key)+" found, adding to total")
        gear_total += mult(val)
        logging.info("Running total: %d" % gear_total)

print("Gear Total: %d" % gear_total)