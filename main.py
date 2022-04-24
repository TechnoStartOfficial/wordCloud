def filter_string(inputString):
    outputString = ""
    for i in inputString:
        if inputString.isalnum():
            outputString+=i
    unwanted = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
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
