import requests, json, urllib

SEARCH_URL = 'http://core.ac.uk:80/api-v2/articles/search/'
API_KEY = 'FILL THIS IN'

def getCOREMentions(identifier, **kwargs):
    """Return the number of mentions in CORE and a descriptor, as a tuple.
    
    Needs an API key, which can be obtained here: http://core.ac.uk/api-keys/register"""
    params = {
        'apiKey': API_KEY,
        'metadata': 'false',
        'pageSize': 100,
        'page': 1
    }
    params.update(kwargs)

    response = requests.get(SEARCH_URL + urllib.quote_plus(identifier), params=params)
    response.raise_for_status()

    results = response.json()

    return (len(results['data'] or []),
            'mentions in Open Access articles (via http://core.ac.uk/)')
