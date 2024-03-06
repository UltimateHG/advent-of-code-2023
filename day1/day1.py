import logging

nums = ["1","2","3","4","5","6","7","8","9","0"]
nums_str = ["one","two","three","four","five","six","seven","eight","nine","zero"]

# logging.getLogger().setLevel(logging.DEBUG)

def parseint(input):
    if input in nums:
        return input
    if input in nums_str:
        return nums[nums_str.index(input)]

# def search_front(input):
#     for char in input:
#         if char in nums:
#             return char

# def search_back(input):
#     reverse = reversed(input)
#     for char in reverse:
#         if char in nums:
#             return char

def search_front(input):
    ans = {}
    logging.info("Finding first occurrence")
    # find digit first
    logging.info("Finding digits")
    for char in input:
        if char in nums:
            ans[char] = input.find(char)
            break
    # find text number
    logging.info("Finding text numbers")
    for num in nums_str:
        found = input.find(num)
        if found > -1:
            ans[num] = found
            logging.info("Number found: "+num)
    # find minimum dict value
    minimum = min(ans, key=ans.get)
    print("Min is "+minimum)
    return parseint(minimum)

def search_back(input):
    ans = {}
    logging.info("Finding last occurrence")
    # find digit first
    logging.info("Finding digits")
    for char in reversed(input):
        if char in nums:
            ans[char] = input.rfind(char)
            break
    # find text number
    logging.info("Finding text numbers")
    for num in nums_str:
        found = input.rfind(num)
        if found > -1:
            ans[num] = found
            logging.info("Number found: "+num)
    # find maximum dict value
    maximum = max(ans, key=ans.get)
    print("Max is "+maximum)
    return parseint(maximum)
        
try:
    with open("input.txt") as f:
        lines = f.readlines()
        answer = 0
        logging.info("Loaded lines, parsing now")
        for line in lines:
            parsed = search_front(line)+search_back(line)
            print("Number formed: "+parsed)
            answer += int(parsed)
            print("Running total: "+str(answer))
        
        print("Final answer: "+str(answer))    
except:
    logging.error("Error")