#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


file_path = r"C:\Users\isha6\Downloads\archive (2)\IMDB Dataset.csv"
df = pd.read_csv(file_path)


# In[5]:


df.head()


# In[6]:


df['review'][3]


# In[7]:


df['review'][3].lower()


# In[9]:


df['review'].str.lower()


# In[10]:


df['review']=df['review'].str.lower()


# In[14]:


import re
def remove_html_tags(text):
    pattern=re.compile('<.*?>')
    return pattern.sub(r'',text)


# In[15]:


text='<html><body>hi isha wassup?</body></html>'
remove_html_tags(text)


# In[16]:


df['review'].apply(remove_html_tags)


# In[17]:


df['review']=df['review'].apply(remove_html_tags)
df


# In[ ]:


#regex used for urls as well (r'https://\S+|www\.\S+)


# In[18]:


import string, time
string.punctuation


# In[21]:


exclude= string.punctuation
def remove_punc(text):
    for char in exclude:
        text=text.replace(char,'')
    return text


# In[22]:


text="hi!! baby how r u? love u, a lottt....."
remove_punc(text)


# In[ ]:


#this takes hell lot of time hence another shortcut


# In[23]:


def remove_punc1(text):
    return text.translate(str.maketrans('','',exclude))
remove_punc1(text)


# In[24]:


acronyms = {
    "AFAIK": "As Far As I Know",
    "AFK": "Away From Keyboard",
    "ASAP": "As Soon As Possible",
    "ATK": "At The Keyboard",
    "ATM": "At The Moment",
    "A3": "Anytime, Anywhere, Anyplace",
    "BAK": "Back At Keyboard",
    "BBL": "Be Back Later",
    "BBS": "Be Back Soon",
    "BFN": "Bye For Now",
    "B4N": "Bye For Now",
    "BRB": "Be Right Back",
    "BRT": "Be Right There",
    "BTW": "By The Way",
    "B4": "Before",
    "B4N": "Bye For Now",
    "CU": "See You",
    "CUL8R": "See You Later",
    "CYA": "See You",
    "FAQ": "Frequently Asked Questions",
    "FC": "Fingers Crossed",
    "FWIW": "For What It's Worth",
    "FYI": "For Your Information",
    "GAL": "Get A Life",
    "GG": "Good Game",
    "GN": "Good Night",
    "GMTA": "Great Minds Think Alike",
    "GR8": "Great!",
    "G9": "Genius",
    "IC": "I See",
    "ICQ": "I Seek you (also a chat program)",
    "ILU": "I Love You",
    "IMHO": "In My Honest/Humble Opinion",
    "IMO": "In My Opinion",
    "IOW": "In Other Words",
    "IRL": "In Real Life",
    "KISS": "Keep It Simple, Stupid",
    "LDR": "Long Distance Relationship",
    "LMAO": "Laugh My A.. Off",
    "LOL": "Laughing Out Loud",
    "LTNS": "Long Time No See",
    "L8R": "Later",
    "MTE": "My Thoughts Exactly",
    "M8": "Mate",
    "NRN": "No Reply Necessary",
    "OIC": "Oh I See",
    "PITA": "Pain In The A..",
    "PRT": "Party",
    "PRW": "Parents Are Watching",
    "QPSA?": "Que Pasa?",
    "ROFL": "Rolling On The Floor Laughing",
    "ROFLOL": "Rolling On The Floor Laughing Out Loud",
    "ROTFLMAO": "Rolling On The Floor Laughing My A.. Off",
    "SK8": "Skate",
    "STATS": "Your sex and age",
    "ASL": "Age, Sex, Location",
    "THX": "Thank You",
    "TTFN": "Ta-Ta For Now!",
    "TTYL": "Talk To You Later",
    "U": "You",
    "U2": "You Too",
    "U4E": "Yours For Ever",
    "WB": "Welcome Back",
    "WTF": "What The F...",
    "WTG": "Way To Go!",
    "WUF": "Where Are You From?",
    "W8": "Wait...",
    "7K": "Sick:-D Laughter"
}


acronyms


# In[27]:


text="roflol you're so cool"
new_text=[]
for x in text.split():
    if x.upper() in acronyms:
        new_text.append(acronyms[x.upper()])
    else:
        new_text.append(x)
print(" ".join(new_text))


# In[ ]:


#spelling mistakes solve karne k lie hume libraries import krne honge unka logic likhne ki need ni h.libraries like:nltk, textBlob


# In[ ]:


#for stop words as well libraries, but in certain sensitive conditions if they're needed like parts of speech then another condition


# In[ ]:


#for emijis we can do import emojis which is a python library


# In[28]:


from nltk.stem.porter import PorterStemmer


# In[30]:


ps= PorterStemmer()
def stem_words(text):
    return ' '.join([ps.stem(word) for word in text.split()])
text="sing singing sang"
stem_words(text)


# In[ ]:




