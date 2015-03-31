# This is a software index handler that gives a score based on the
# number of mentions in open access articles.  It uses the CORE
# aggregator (http://core.ac.uk/) to search the full text of indexed
# articles.
# 
# Inputs:
# - identifier (String)
# 
# Outputs:
# - score (Number)
# - description (String)

import requests, urllib

SEARCH_URL = 'http://core.ac.uk:80/api-v2/search/'

class coreapi_handler:

    def get_score(self, software_identifier, key, **kwargs):
        """Return the number of mentions in CORE and a descriptor, as a tuple.

        Needs an API key, which can be obtained here: http://core.ac.uk/api-keys/register"""
        if isinstance(software_identifier, basestring):
            params = {
                'apiKey': key,
            }
            params.update(kwargs)

            response = requests.get(SEARCH_URL + urllib.quote_plus(software_identifier), params=params)
            response.raise_for_status()

            results = response.json()
            score = results['totalHits']

            return score
        else:
            return -1

    def get_description(self):
        return 'mentions in Open Access articles (via http://core.ac.uk/)'
