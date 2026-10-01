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

# Step 4 - normalize_text
import unicodedata
import re

def normalize_text(text):
    # TODO: NFKC-normalize the text and collapse runs of whitespace into single spaces.
    normalized = unicodedata.normalize("NFKC", text)

    content = re.sub(r"\s+", " ", normalized)

    cleaned = content.strip()

    return cleaned

# Step 5 - make_document
def make_document(text, source, title):
    # TODO: wrap text with source and title metadata into a document dict.
    document = {
        "text" : text,
        "source" : source,
        "title" : title
    }

    return document

# Step 6 - chunk_fixed_size
def chunk_fixed_size(text, chunk_size):
    # TODO: split text into consecutive non-overlapping chunks of length chunk_size
    chunks = []

    for start in range(0, len(text), chunk_size):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks

# Step 7 - chunk_by_tokens
def chunk_by_tokens(text, tokenizer, max_tokens):
    # TODO: split text into chunks of at most max_tokens token ids using the tokenizer

    if not text:
        return []

    tokens = tokenizer.encode(text, add_special_tokens=False)

    chunks = []

    for start in range(0, len(tokens), max_tokens):
        token_chunk = tokens[start:start + max_tokens]

        chunk = tokenizer.decode(token_chunk)

        chunks.append(chunk)

    return chunks

