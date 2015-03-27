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

SEARCH_URL = 'http://core.kmi.open.ac.uk/api/search/'
API_KEY = 'FILL THIS IN'

class core_handler:

    def get_score(self, identifier, **kwargs):
        """Return the number of mentions in CORE and a descriptor, as a tuple.

        Needs an API key, which can be obtained here: http://core.ac.uk/api-keys/register"""

        params = {
            'api_key': API_KEY,
            'format': 'json',
        }
        params.update(kwargs)

        response = requests.get(SEARCH_URL + urllib.quote_plus(identifier), params=params)
        response.raise_for_status()

        results = response.json()
        score = results['ListRecords'][0]['total_hits']

        return score 

    def get_description(self):
        return 'mentions in Open Access articles (via http://core.ac.uk/)'
