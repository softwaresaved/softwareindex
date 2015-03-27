# This is a software index handler that gives a score based on the
# number of mentions in SlideShare. It uses the SlideShare API:
# http://www.slideshare.net/developers/documentation
# 
# Inputs:
# - Identifier (String)
# 
# Outputs:
# - score (Number)
# - description (String)
#
# Notes: this handler treats the software identifier as a string, 
# even if it is a URL represented as a string. The behaviour of the
# SlideShare API for this has not been tested

import time, urllib, urllib2
from hashlib import sha1
from bs4 import BeautifulSoup

SEARCH_URL = 'https://www.slideshare.net/api/2/search_slideshows'
MATCH_STRING = 'TotalResults'


class slideshare_handler:

    def get_score(self, identifier, key, secret, **kwargs):
        """ Return the number of mentions in SlideShare and a descriptor
        Needs an API key, which can be obtained here:
        http://www.slideshare.net/developers/applyforapi """

        ts = int(time.time())
        strts = str(ts)

        params = {
            'api_key' : key,
            'ts' : strts,
            'hash' : sha1(secret+strts).hexdigest(),
            'q' : identifier,
        }
        params.update(kwargs)        
   
        response = urllib2.urlopen(SEARCH_URL + '?' + urllib.urlencode(params))
        soup = BeautifulSoup(response, 'xml')
        return soup.find(MATCH_STRING).string

    def get_description(self):
        return 'Score based on number of mentions of software identifier in SlideShare'
