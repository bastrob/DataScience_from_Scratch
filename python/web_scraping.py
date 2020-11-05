# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:48:34 2020

@author: Bast
"""

# Install:
# python -m pip install beautifulsoup4 requests html5lib

from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/bastrob/DataScience_from_Scratch/master/python/simple_html.html")

html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")


# Retrieve first parapagh
first_paragraph = soup.find('p')

print(first_paragraph)

# Extract the whole text of first paragraph
first_paragraph_text = soup.p.text
print(first_paragraph_text)

# Split words into list
first_paragraph_words = soup.p.text.split()
print(first_paragraph_words)

# Extract a tag attribute
first_paragraph_id = soup.p["id"] # Raises KeyError if no 'id' found
first_paragraph_id2 = soup.p.get("id") # Returns None if no 'id' found

print(first_paragraph_id)


all_paragraph = soup.find_all('p') # or soup("p")
paragraph_with_ids = [p for p in soup("p") if p.get("id")]

print(paragraph_with_ids)


# Find tags with a specific class
important_paragraphs = soup("p", {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]

print(important_paragraphs)

#Combine methods
# Example: Find every <span> element contained inside a <div> element
spans_inside_divs = [span 
                     for div in soup("div")
                     for span in div("span")]


#Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# Exercise: find all the representatives who have press releases about data
url = ("https://www.house.gov/representatives")
html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")

all_urls = [a["href"]
            for a in soup("a") if a.has_attr('href')]

print(len(all_urls)) #Size: 966

# We need to extract only URLs starting by http or https and end with .house.gov or .house.gov/
#print(all_urls)


# Good place to apply regular expression

# https://docs.python.org/3/library/re.html
import re

# Must start with http:// or https://
# Must end with .house.gov or .house.gov/
# ^: matches the start of the string
# ?: https? matches http or https
# .*: matches any url 
# \: special content to match
# \.gov/?: special content to match + either gov or gov/
# $: specifies the end of the match, every url with suppl http://barky.house.gov/XXxx will not be matched

#regex = r"^https?://.*\.house\.gov/?$"
regex = r"^http(s)?://.*\.house\.gov/?$"
#regex_test = r"^http://"

# Test code
assert re.match(regex, "http://barky.house.gov")
assert re.match(regex, "http://barky.house.gov/")
assert re.match(regex, "https://barky.house.gov")
assert re.match(regex, "https://barky.house.gov/")

assert not re.match(regex, "http://house.gov.barky")
assert not re.match(regex, "/sitemap")
assert not re.match(regex, "http://barky.data.com")
assert not re.match(regex, "https://barky.data")
assert not re.match(regex, "http://barky.house.gov/data")
assert not re.match(regex, "https://barky.house.gov/data")


good_urls = [url for url in all_urls if re.match(regex, url)]

print(len(good_urls)) # Size: 872
print(good_urls)


