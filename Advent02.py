import re
file_path = 'AdventText01.txt'

def extractNumbersFromString(text : str):
    empty_list = []
    frontFound = False
    endFound = False
    returnValue = ""
    newWord = ""
    number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number_digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for j in range(len(text)):
        if(frontFound):
            break
        newWord += text[j]
        for i in range(0, 9):
                checkagainst = number_words[i]
                checkagainstdigit = number_digit[i]
                if checkagainst in newWord or checkagainstdigit in newWord:
                    empty_list.append(number_digit[i])           
                    newWord = ""
                    frontFound = True
                    break
                else:
                    continue
                
    for j in range(len(text) - 1, -1, -1):
        if(endFound):
            break
        newWord += text[j]
        for i in range(0, 9):
                reversedString = newWord[::-1]
                checkagainst = number_words[i]
                checkagainstdigit = number_digit[i]
                if checkagainst in reversedString or checkagainstdigit in reversedString:
                    empty_list.append(number_digit[i])           
                    endFound = True
                    break
                else:
                    continue

        
    
    if(len(empty_list) == 0):
        return 0
    elif(len(empty_list) == 1):
        returnValue += empty_list[0] + empty_list[0]
        return int(returnValue)
    if(len(empty_list) > 1):
        returnValue += empty_list[0] + empty_list[-1]
        return int(returnValue)


def readList2():
    summary = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                summary += extractNumbersFromString(line)

                print(summary)
    except FileNotFoundError:
        print("File not found")

readList2()