from pytray.TrayConnexion import TrayConnexion
import time

t = TrayConnexion("localhost", 5000, 0 )
print t.SD_INFO( '2333.HK', 'lastclose' )
# print t.SD_INFO( '2333.HK', 'address' )
# print t.SD( '2333.HK', 'eps', 2016 )

# print t.SD_INDUSTRY_LIST()
# print t.SD_SECTOR_LIST('Automotive')
# print t.SD_COMPANY_LIST( 'Automotive', 'Automobiles')
# print t.SD_COMPANY_LIST( 'Automotive', 'Automobiles', 'HK')

print t.SD_QUOTE( '2333.HK', 'close_adj', '2017-03-21' )
