#!/usr/bin/env python
# coding: utf-8

# In[5]:


with open("un_declaration_hr_text_data.txt", "r") as file:
    declaration_text = file.read()


# In[9]:


import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Remove unwanted characters and convert to lowercase
clean_text = re.sub(r"[^\w\s]", "", declaration_text.lower())

# Tokenize the text into words
tokens = word_tokenize(clean_text)

# Remove stop words
stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word not in stop_words]


# ##### Generate a Word Cloud of the most frequent terms:

# In[1]:


from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

# Read text
text = open('un_declaration_hr_text_data.txt', mode="r", encoding="utf-8").read()
stopwords = STOPWORDS

wc = WordCloud(font_path='C:\\Users\\gmanc\\Videos\\Hazel\\New folder\\uchrony-sc-font\\UchronyScLight-d929X.ttf', background_color='white', stopwords=stopwords, height=600, width=400)
wc.generate(text)

# store to file
wc.to_file("word_cloud.png")


# ##### Generate a bar plot of the top 25 frequent terms:

# In[19]:


from collections import Counter

# Count word occurrences
word_counts = Counter(filtered_tokens)

# Get the top 25 frequent terms
top_terms = word_counts.most_common(25)

# Extract the terms and their counts
terms, counts = zip(*top_terms)

# Create the bar plot
plt.figure(figsize=(12, 6))
plt.bar(terms, counts)
plt.xticks(rotation=90)
plt.xlabel("Terms")
plt.ylabel("Frequency")
plt.title("Top 25 Frequent Terms in UN Declaration of Human Rights")
plt.show()


# In[ ]:




