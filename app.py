#!/usr/bin/python3
"""
Openai terminal interface
"""
import openai
import sys
import json

def load_key(filename):
    """load api key from file
    file must contain openai api key in json string
    """
    if not isinstance(filename, str):
        print('Error: Invalid file name')
        print('Exitin...')
        sys.exit(1)
    try:
        with open(filename, 'r') as fp:
            return json.load(fp)
    except FileNotFoundError:
        print('Error: could not find file key.json')
        print('exiting...')
        sys.exit(1)

def get_result(prompt=''):
    """get Completion from davinci"""
    response = openai.Completion.create(prompt=prompt, model='text-davinci-003', temperature=0.5, n=1, max_tokens=1700)
    return response.choices[0].text

def main():
    """main entry"""
    if len(sys.argv) == 1:
        print('Error: no prompt given')
        sys.exit(1)
    openai.api_key = load_key('key.json')
    prompt = sys.argv[1]
    result = get_result(prompt)
    print(result.strip())


if __name__ == '__main__':
    main()
