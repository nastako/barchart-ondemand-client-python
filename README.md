## Python client for Barchart OnDemand

Get access to market data and the OnDemand APIs in just a few lines of code.

### Installation

```
python setup.py install
```

### Usage

```python
import ondemand

od = ondemand.OnDemandClient(api_key='CHANGE_ME')

# get quote data for Apple and Microsoft
quotes = od.quote('AAPL,MSFT')['results']

for q in quotes:
    print('Symbol: %s, Last Price: %s' % (q['symbol'], q['lastPrice']))

# get 1 minutes bars for Apple
resp = od.history('AAPL', 'minutes', maxRecords=50, interval=1)

# generic request by API name
resp = od.get('getQuote', symbols='AAPL,EXC', fields='bid,ask')
```

### Version

- 1.0 - 7/27/2017 -- init