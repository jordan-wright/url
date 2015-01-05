import sys
import argparse
import urlparse

# url.py
# version 0.1
# Author: Jordan Wright <github.com/jordan-wright>

# Notes: Ideally, we'll want to incorporate a TLD Extract module at some point

scheme_port_dict = {
    'ftp' : 21,
    'ssh' : 22,
    'smtp' : 25,
    'http' : 80,
    'https': 443
}

class URL (urlparse.ParseResult):
    def __new__(cls, url):
        parse_result = urlparse.urlparse(url)
        return super(URL, cls).__new__(cls, *parse_result)

    def __init__(self, url):
        self.url = url
        # Get the TLD (close enough)
        self.tld = self.netloc.split(".")[-1] # not perfect by any means.
        self.host = self.netloc.split(".")[-2] # not perfect
        self.subdomain = '.'.join(self.netloc.split(".")[0:-2]) # not perfect
        # Set the default port for the service if none provided
        #if not self.port and scheme_port_dict.get(self.scheme):
        #    self.port = self._replace(port=scheme_port_dict[self.scheme])

    def __str__(self):
        return self.url

if __name__ == "__main__":
    # Setup the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scheme', action='store_true', help='Include the URL scheme')
    parser.add_argument('-c', '--sub', action='store_true', help='Include the URL subdomain')
    parser.add_argument('-d', '--domain', action='store_true', help='Include the URL host and TLD')
    parser.add_argument('-n', '--host', action='store_true', help='Include the URL host only (no TLD)')
    parser.add_argument('-t', '--tld', action='store_true', help='Include the URL TLD')
    parser.add_argument('-pt', '--port', action='store_true', help='Include the URL port')
    parser.add_argument('-pa', '--path', action='store_true', help='Include the URL path')
    parser.add_argument('-ps', '--params', action='store_true', help='Include the URL params')
    parser.add_argument('-q', '--query', action='store_true', help='Include the URL query')
    parser.add_argument('-f', '--frag', action='store_true', help='Include the URL fragment')
    parser.add_argument('-a', '--all', action='store_true', help='Include the full URL')
    args = parser.parse_args()

    # enumerate through stdin
    for line in sys.stdin:
        line = line.rstrip()
        if args.all:
            print line
            continue
        url = URL(line)
        if args.scheme:
            print url.scheme
        if args.scheme and args.domain:
            print url.scheme + '://' + url.domain
        elif args.domain:
            print url.domain
