def filter_string(inputString):
    outputString = ""
    for i in inputString:
        if inputString.isalnum():
            outputString+=i
    unwanted = ['if','but','why','no','hence','although']
    for i in unwanted:
        outputString=outputString.replace(i,"")
    return outputString
def text_count(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
