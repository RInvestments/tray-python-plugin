# Python Interface for tray-api

### See:
[https://github.com/RInvestments/sun-dance](https://github.com/RInvestments/sun-dance)<br/>
[https://github.com/RInvestments/tray-api](https://github.com/RInvestments/tray-api)

With sun-dance repo crawl the data and insert into mongodb. With tray-api repo,
set up the restful API on the server. Finally this provides a package to retrive data with ease.

If you plan to use this, you need to setup 'sun-dance' and 'tray-api'. The tray-api server need
to be running for these queries to work. I have structured it such, for purpose of modularity,
and so that the financial modelling part remains totally separated from data related engineering
and database queries. For real modelling task you need to set this package in PYTHONPATH and
you are good to go.

### Dependencies:
urllib2


### Example Usage of this package
```
from pytray.TrayConnexion import TrayConnexion

# Establish connection
t = TrayConnexion("localhost", 5000, 0 )

# Query for latest available price
print t.SD_INFO( '2333.HK', 'lastclose' )

# Query address of the ticker
print t.SD_INFO( '2333.HK', 'address' )

# Get ticker's financial sheets info
print t.SD( '2333.HK', 'eps', 2016 )

# List API
print t.SD_INDUSTRY_LIST()
print t.SD_SECTOR_LIST('Automotive')
print t.SD_COMPANY_LIST( 'Automotive', 'Automobiles')
print t.SD_COMPANY_LIST( 'Automotive', 'Automobiles', 'HK')

# Quote data API
print t.SD_QUOTE( '2333.HK', 'close_adj', '2017-03-21' )
```

### TODO
Keep this pythong wrapper uptodate with the API.

Work on improving query times for each query. Currently quotes query takes 15ms which is bit high. Financial info query takes 3ms. Slightly high but acceptable. Most of the time is consumed by the urllib2 query. Know more to optimize it.
