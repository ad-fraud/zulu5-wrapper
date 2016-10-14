# - depending on your system youu may have to 'pip install' some libraries
# - the expectation is that you have the zulu5 JSON saved in a file 'ads.json' 

import json
from urllib2 import Request, urlopen

x = {}

with open('ads.json') as fp:
    for line in fp:
        x.update(json.loads(line))
        
rows = len(x['items'])

d = pd.DataFrame(columns = ['ClickUrl','Url'])

for i in range(rows):
    
    parsed_uri = urlparse(x['items'][i]['clickUrl'])
    parsed_site = urlparse(x['items'][i]['url'])
    
    d.ClickUrl.at[i] = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    d.Url.at[i] = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_site)
    
referrers = len(pd.Series.value_counts(d.Url))
advertisers = len(pd.Series.value_counts(d.ClickUrl))
sorted_referrers = pd.Series.value_counts(d.Url)
sorted_advertisers = pd.Series.value_counts(d.ClickUrl)
