import requests, json, urllib

SEARCH_URL = 'http://core.kmi.open.ac.uk/api/search/'
API_KEY = 'FILL THIS IN'

def getCOREMentions(identifier, **kwargs):
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

    return score, 'mentions in Open Access articles (via http://core.ac.uk/)'
