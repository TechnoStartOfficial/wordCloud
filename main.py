from wordcloud import WordCloud
import matplotlib.pyplot as plt
def filter_string(inputString):
    cleanString=""
    for i in inputString:
        if i.isalnum() or i == " ":
            cleanString+=i
    cleanList = cleanString.split()
    unwantedChars = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
        "all", "any", "both" , "1","2","3","4","5","6","7","8","9", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    for i in unwantedChars:
        for j in range(0,len(cleanList)):
            if i == cleanList[j]:
                cleanList[j]=""
    return " ".join(cleanList)
f = open("text.txt","r").read()
wc = WordCloud(background_color="white",max_font_size=50,max_words=100)
wc.generate(filter_string(f))
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()
