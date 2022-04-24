def filter_string(inputString):
    outputString = ""
    for i in inputString:
        if inputString.isalnum():
            outputString+=i
    unwanted = ['if','but','why','no','hence','although']
    for i in unwanted:
        outputString=outputString.replace(i,"")
    return outputString
