#!/usr/bin/env python3

from urllib.request import urlopen
import sys


def fetch_words(url):
    with urlopen(url) as story:
        story_words_bytes = []
        story_words_str = []
        for line in story:
            line_words_bytes = line.split()
            line_words_str = line.decode('utf-8').split()
            for word in line_words_bytes:
                story_words_bytes.append(word)
            for word in line_words_str:
                story_words_str.append(word)
        print(story_words_bytes)
        print(story_words_str)


def convert(s):
    """Convert a string to an integer."""
    if not isinstance(s, str):
        raise TypeError("Argument must be a string".)
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise


def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.

    Returns:
        The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot compute square root of negativenumber{}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

if __name__ == '__main__':
    url = 'http://sixty-north.com/c/t.txt'
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(f'URL passed: {url}')
    else:
        print(f'Arguments not entered. Default URL: {url}')
    fetch_words(url)
    try:
        sqrt(-1)
    except ValueError:
        print('Let it go.')
    try:
        convert('fail')
    except ValueError:
        print('Let this also go.')
