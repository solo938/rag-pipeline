"""
RAG Pipeline

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - load_text_file
def load_text_file(path):
    # TODO: read a UTF-8 text file at `path` and return its contents as one string.
    file = open(path, "r", encoding="utf-8")
    content = file.read()

    return content

# Step 2 - load_text_directory
import os
def load_text_directory(directory):
    # TODO: read every .txt file in `directory` and return their contents as a list of strings
    contents = []

    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, "r", encoding="UTF-8") as file:
                content = file.read()
                contents.append(content)
    
    return contents

# Step 3 - extract_text_from_html
from html.parser import HTMLParser

def extract_text_from_html(html):
    class TextParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text = []
            self.skip = False

        def handle_starttag(self, tag, attrs):
            if tag == "script" or tag == "style":
                self.skip = True

        def handle_endtag(self, tag):
            if tag == "script" or tag == "style":
                self.skip = False

        def handle_data(self, data):
            if not self.skip:
                self.text.append(data)

    parser = TextParser()
    parser.feed(html)

    return "".join(parser.text).strip()

