#!/usr/bin/python3
"""
Openai terminal interface
"""

def load_json(filename):
    if not isinstance(filename, str):
        raise TypeError("Invalid filename")
    try:
        with open(filename, 'r') as fp:
            return json.load(fp)
    except 
