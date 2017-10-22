## The main class which can connect to the API
import urllib2
import time

class TrayConnexion:
    def __init__( self, server=None, port=None, debug=0 ):
        """ Server URL (default:localhost), Server Port (default:5000), debug level. 0 for no debug, 5 for max debug """
        self.server = server
        self.port = port
        self.debug_lvl = debug

        if self.server is None:
            self.server = 'localhost'

        if self.port is None:
            self.port = str(5000)

    def __str__(self):
        print self._server_url()

    def _server_url( self ):
        return 'http://%s:%s' %(self.server, self.port)

    def _debug( self, txt, lvl=0 ):
        if lvl in range(self.debug_lvl):#[0,1,2,3,4,5]:
            print '(Debug=%2d) :' %(lvl), txt

    def _download( self, url ):
        """ Returns the contents of the URL as a string. You need to convert it to int by yourself """

        if url is None:
            self._debug( 'URL is None, Skipping...' )
            return None

        self._debug( 'download :'+ url )
        try:
            startDownload = time.time()
            html = urllib2.urlopen( url ).read() #if timeout happens rerun the script should be able to recover
            self._debug( 'Downloaded in %4.2f ms' %( 1000.* (time.time() - startDownload ) ) )
            return html
        except:
            return None


    ########### TICKER INFO #############
    def SD_INFO( self, ticker, field ):
        """ To get timeless info about a ticker """
    	url_db = {}
    	url_db['name'] = '/api/info/%s' %(ticker)
    	url_db['industry'] = '/api/info/%s/industry' %(ticker)
    	url_db['sector'] = '/api/info/%s/sector' %(ticker)
    	url_db['employees'] = '/api/info/%s/employees' %(ticker)
    	url_db['description'] = '/api/info/%s/description' %(ticker)
    	url_db['address'] = '/api/info/%s/address' %(ticker)




    	url_db['quote_lastclose'] = '/api/info/%s/quote/close' %(ticker)
    	url_db['lastclose'] = url_db['quote_lastclose']
    	url_db['quote_lastvolume'] = '/api/info/%s/quote/volume' %(ticker)
    	url_db['lastvolume'] = url_db['quote_lastvolume']
    	url_db['quote_lastdatetime'] = '/api/info/%s/quote/datetime' %(ticker)
    	url_db['lastdatetime'] = url_db['quote_lastdatetime']

    	if str(field) in url_db.keys():
    		URL = self._server_url()+url_db[field]
    		return self._download( URL )
        else:
            self._debug( 'Invalid field in SD_INFO()' )
            return None

    def SD( self, ticker,field,year ):
        """ To get timed financial sheets info about a ticker """

    	url_db = {}
    	# From Income Statement
    	url_db['revenue'] = '/api/info/%s/is/revenue/%d' %(ticker,year)
    	url_db['cogs' ] = '/api/info/%s/is/cogs/%d' %(ticker,year)
    	url_db['income_gross' ] = '/api/info/%s/is/income_gross/%d' %(ticker,year)
    	url_db['income_pretax' ] = '/api/info/%s/is/income_pretax/%d' %(ticker,year)
    	url_db['income_net' ] = '/api/info/%s/is/income_net/%d' %(ticker,year)
    	url_db['expense_sga' ] = '/api/info/%s/is/expense_sga/%d' %(ticker,year)
    	url_db['expense_interest' ] = '/api/info/%s/is/expense_interest/%d' %(ticker,year)
    	url_db['expense_tax' ] = '/api/info/%s/is/expense_tax/%d' %(ticker,year)
    	url_db['ebit' ] = '/api/info/%s/is/ebit/%d' %(ticker,year)
    	url_db['ebitda' ] = '/api/info/%s/is/ebitda/%d' %(ticker,year)
    	url_db['eps' ] = '/api/info/%s/is/eps/%d' %(ticker,year)
    	url_db['eps_basic' ] = '/api/info/%s/is/eps_basic/%d' %(ticker,year)
    	url_db['eps_diluted' ] = '/api/info/%s/is/eps_diluted/%d' %(ticker,year)
    	url_db['shares_outstanding' ] = '/api/info/%s/is/shares_outstanding/%d' %(ticker,year)


    	# From Balance SHeet/Assets
    	url_db['total_assets'] = '/api/info/%s/bs/total_assets/%d' %(ticker,year)
    	url_db['total_current_assets'] = '/api/info/%s/bs/total_current_assets/%d' %(ticker,year)
    	url_db['total_accounts_receivable'] = '/api/info/%s/bs/total_accounts_receivable/%d' %(ticker,year)
    	url_db['inventories'] = '/api/info/%s/bs/inventories/%d' %(ticker,year)
    	url_db['ppe'] = '/api/info/%s/bs/ppe/%d' %(ticker,year)
    	url_db['other_current_assets'] = '/api/info/%s/bs/other_current_assets/%d' %(ticker,year)
    	url_db['cash'] = '/api/info/%s/bs/cash/%d' %(ticker,year)
    	url_db['short_term_investments'] = '/api/info/%s/bs/short_term_investments/%d' %(ticker,year)

    	url_db['total_investment_advances'] = '/api/info/%s/bs/total_investment_advances/%d' %(ticker,year)
    	url_db['long_term_receivable'] = '/api/info/%s/bs/long_term_receivable/%d' %(ticker,year)
    	url_db['intangible_assets'] = '/api/info/%s/bs/intangible_assets/%d' %(ticker,year)
    	url_db['other_assets'] = '/api/info/%s/bs/other_assets/%d' %(ticker,year)

    	# From Balance sheet/Liabilities
    	url_db['debt_payment_short_term'] = '/api/info/%s/bs/debt_payment_short_term/%d' %(ticker,year)
    	url_db['debt_payment_long_term'] = '/api/info/%s/bs/debt_payment_long_term/%d' %(ticker,year)
    	url_db['accounts_payable'] = '/api/info/%s/bs/accounts_payable/%d' %(ticker,year)
    	url_db['income_tax_payable'] = '/api/info/%s/bs/income_tax_payable/%d' %(ticker,year)
    	url_db['other_current_liabilities'] = '/api/info/%s/bs/other_current_liabilities/%d' %(ticker,year)
    	url_db['total_current_liabilities'] = '/api/info/%s/bs/total_current_liabilities/%d' %(ticker,year)
    	url_db['other_liabilities'] = '/api/info/%s/bs/other_liabilities/%d' %(ticker,year)
    	url_db['total_liabilities'] = '/api/info/%s/bs/total_liabilities/%d' %(ticker,year)

    	# From cash_flow_statement
    	url_db['net_operating_cashflow'] = '/api/info/%s/cf/net_operating_cashflow/%d' %(ticker,year)

    	url_db['net_investing_cashflow'] = '/api/info/%s/cf/net_investing_cashflow/%d' %(ticker,year)
    	url_db['capital_expense'] = '/api/info/%s/cf/capital_expense/%d' %(ticker,year)
    	url_db['acquisitions'] = '/api/info/%s/cf/acquisitions/%d' %(ticker,year)
    	url_db['sale_of_assets'] = '/api/info/%s/cf/sale_of_assets/%d' %(ticker,year)
    	url_db['from_financial_instruments'] = '/api/info/%s/cf/from_financial_instruments/%d' %(ticker,year)

    	url_db['net_financing_cashflow'] = '/api/info/%s/cf/net_financing_cashflow/%d' %(ticker,year)
    	url_db['free_cashflow'] = '/api/info/%s/cf/free_cashflow/%d' %(ticker,year)
    	url_db['net_change_in_cash'] = '/api/info/%s/cf/net_change_in_cash/%d' %(ticker,year)
    	url_db['dividend_paid'] = '/api/info/%s/cf/dividend_paid/%d' %(ticker,year)
    	url_db['debt_reduction'] = '/api/info/%s/cf/debt_reduction/%d' %(ticker,year)

        if str(field) in url_db.keys():
            URL = self._server_url()+url_db[field]
            # print URL
            return self._download( URL )
        else:
            self._debug( 'Invalid field in SD()')
            return None

    def SD_QUOTE( self, ticker,field, sp_date ):
        """ Returns the stock price of a ticker on a specified date. Currently only daily quotes.
        sp_date in '%Y-%m-%d' format. example 2017-02-23
        """
        url_db = {}
        # From Daily Quote Data
        url_db['close' ] = '/api/info/%s/quote/close/%s' %(ticker,( sp_date ))
        url_db['close_adj' ] = '/api/info/%s/quote/close_adj/%s' %(ticker,( sp_date ))
        url_db['volume' ] = '/api/info/%s/quote/volume/%s' %(ticker,( sp_date ))
        url_db['datetime' ] = '/api/info/%s/quote/datetime/%s' %(ticker,( sp_date ))
        url_db['inserted_on' ] = '/api/info/%s/quote/inserted_on/%s' %(ticker,( sp_date ))
        url_db['open' ] = '/api/info/%s/quote/open/%s' %(ticker,( sp_date ))
        url_db['high' ] = '/api/info/%s/quote/high/%s' %(ticker,( sp_date ))
        url_db['low' ] = '/api/info/%s/quote/low/%s' %(ticker,( sp_date ))

    	if str(field) in url_db.keys():
    		URL = self._server_url()+url_db[field]
    		return self._download( URL )
        else:
            self._debug( 'Invalid field in SD_QUOTE()' )
            return None

    ########## LIST returning functions ############
    def SD_INDUSTRY_LIST( self ):
        """ Get list of industry """
    	URL = self._server_url()+'/api/list/industry_list'
    	industry_list_csv = self._download( URL )
        li = industry_list_csv.split(',')
        self._debug( 'Found %d elements' %(len(li) ))
        return li


    def SD_SECTOR_LIST( self, industry_name ):
        """ Given an industry, returns sections of this industry """
    	URL = self._server_url()+'/api/list/%s/sector_list' %( industry_name.replace("/","_") )
        sector_list_csv = self._download( URL )
        li = sector_list_csv.split( ',' )
        self._debug( 'Found %d elements' %(len(li)) )
        return li


    def SD_COMPANY_LIST( self, industry, sector, bourse=None ):
        """ Given an Industry and a sector, split of all the companies tickers.
            Not giving bourse will cause it to return for all exchanges
        """
        if bourse is None:
            URL = self._server_url()+'/api/list/%s/%s/company_list/' %(industry.replace("/","_"),sector.replace("/","_") )
        else:
        	URL = self._server_url()+'/api/list/%s/%s/company_list/%s' %(industry.replace("/","_"),sector.replace("/","_"),bourse )
        company_list_csv = self._download( URL )
        li = company_list_csv.split( ',' )
        self._debug( 'Found %d companies for (%s), (%s) of bourse %s' %(len(li), industry, sector, str(bourse)))

        return li
