import re

file_path = 'C:/Users/ureke/Desktop/myfile.txt'

# Open the file and read it line by line

def extractFirstandLast(digits_str : str):
    first_digit = digits_str[0]
    
    if len(digits_str) == 1:
        first_digit += first_digit
        return int(first_digit)
    else:
        last_digit = digits_str[-1]
        first_digit += last_digit
        return int(first_digit)
        
    
    
def readList():
    summary = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                digits = re.findall(r'\d+', line)
                if not digits:
                    continue
                digitsJoined = ''.join(digits)
                summary += extractFirstandLast(digitsJoined)

                print(summary)
    except FileNotFoundError:
        print("File not found")
        

#readList()