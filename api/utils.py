class NumberTooLargeError(Exception):
    pass

def number_to_english(n):
    if n == 0:
        return "zero"
    
    MAX_NUMBER = 10**12 - 1  # define an upper limit (trillion - 1) 999,999,999,999 

    if n > MAX_NUMBER:
        raise NumberTooLargeError("Number is too large to process")
    
    units = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    multiplier = ["", "thousand", "million", "billion"]
    
    res = ""
    group = 0
    
    while n > 0:
        if n % 1000 != 0:
            
            value = n % 1000
            temp = ""
            
            if value >= 100:
                temp = units[value // 100] + " hundred "
                value %= 100

            if value >= 20:
                temp += tens[value // 10] + " "
                value %= 10

            if value > 0:
                temp += units[value] + " "

            temp += multiplier[group] + " "
            res = temp + res
        n //= 1000
        group += 1
    
    return res.strip()