import re
import string
def remove_emojis(data):
    emoj = re.compile("["
      u"\U0001F600-\U0001F64F"  # emoticons
      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
      u"\U0001F680-\U0001F6FF"  # transport & map symbols
      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
      u"\U00002500-\U00002BEF"  # chinese char
      u"\U00002702-\U000027B0"
      u"\U00002702-\U000027B0"
      u"\U000024C2-\U0001F251"
      u"\U0001f926-\U0001f937"
      u"\U00010000-\U0010ffff"
      u"\u2640-\u2642" 
      u"\u2600-\u2B55"
      u"\u200d"
      u"\u23cf"
      u"\u23e9"
      u"\u231a"
      u"\ufe0f"  # dingbats
      u"\u3030"
                    "]+", re.UNICODE)
    return re.sub(emoj, '', data)


def remove_trailing_hashtags(tweet):
    # split the tweet into words
    words = tweet.split()
    # iterate over the words in reverse order
    for i in range(len(words)-1, -1, -1):
        # check if the word is a hashtag
        if words[i].startswith("#"):
            # remove the hashtag
            words.pop(i)
        else:
            # if the word is not a hashtag, break the loop
            break
    # join the words back into a string and return it
    return " ".join(words)

def remove_heading_hashtags(tweet):
    # split the tweet into words
    words = tweet.split()
    # iterate over the words in reverse order
    for i in range(len(words)):
        # check if the word is a hashtag
        if words[i].startswith("#"):
            # remove the hashtag
            words.pop(i)
      
        else:
            # if the word is not a hashtag, break the loop
            break
    # join the words back into a string and return it
    return " ".join(words)

def clean_text(text, stop_words):

    text = re.sub(r'@\w+', '', text)
    text = remove_heading_hashtags(text)
    text = remove_trailing_hashtags(text)

    
    text = text.replace("،"," ")
    text = text.replace(","," ")
    text = text.replace("_"," ")
    
    # remove mentions
    
    # remove emojis
    text = remove_emojis(text)

    

    for substring in stop_words:
     text = text.replace(substring, " ")
    
    # delete all english characters
    text = re.sub(r'\s*[A-Za-z]+\b', '' , text)
    text = text.translate(str.maketrans('', '', string.punctuation+"؟"+"."+"،"))
    # delete extra spaces
    text = text.replace("\n"," ")
    text = (re.sub("  +"," ",text)).lower()

    if len(text) < 3:
        return None

    return text