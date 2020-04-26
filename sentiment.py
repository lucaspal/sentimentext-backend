#!/usr/bin/env python3.7

import argparse
import csv
import sys

from newspaper import Article
from textblob import TextBlob

def sentiment(text):
    return TextBlob(text).sentiment

def scrape(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.title, article.text, None
    except Exception as err:
        return "", "", err

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv')
    parser.add_argument('--url', nargs='+')
    parser.add_argument('--csvfields', nargs='+', default=['title', 'text'])
    args = parser.parse_args()
    
    if args.csv is not None:
        reader = csv.reader(open(args.csv))
        header = next(reader)
        indexes = [header.index(f) for f in args.csvfields]
        texts = ([line[i] for i in indexes] for line in reader)
    elif args.url is not None:
        texts = (scrape(url) for url in args.url)
    else:
        texts = ((line,) for line in sys.stdin)
    
    for elems in texts:
        print('='*72)
        for elem in elems:
            print(elem)
            print(sentiment(elem))
