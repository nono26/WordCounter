"""Retrieve and print words from an url.

Usage:
    python words.py <url>
"""

import sys
from urllib.request import urlopen

def fech_words(url):
    """Fetch a list of words from an URL

    Args:
        url: The url of the UTF-8 document

    Returns:
        a list a string containing the words from the document

    """
    story = urlopen(url)
    story_word=[]
    for line in story:
        line_words= line.decode('utf-8').split()
        for word in line_words:
            story_word.append(word)
    story.close()

    return story_word

def print_items(items):
    """Print item from a list of items, one per line

    Args:
        items: array of object
    """

    for item in items:
        print (item)
    
def main(url):
    """Print each words from text document from at a url

    Args:
        url: the url of the UTF-8 document 
    """
    
    words= fech_words(url)
    print_items(words)

if __name__== '__main__':
    main(sys.argv[1])