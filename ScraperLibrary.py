from EbayItemScraper import EbayItemScraper # Used to import the EbayItemScraper class to create an object
from AmazonItemScraper import AmazonItemScraper # Used to import the AmazonItemScraper class to create an object
from EbaySearchResultsScraper import EbaySearchResultsScraper # Used to import the EbaySearchResultsScraper class to create an object
from AmazonSearchResultsScraper import AmazonSearchResultsScraper # Used to import the AmazonSearchResultsScraper class to create an object

# @brief Library class to manage all of the different scraper objects
class ScraperLibrary:

    ## Initialize the Scraper Library object
    def __init__(self):
        self.name = "ScraperLibrary"
        self.EbayItemScraper = EbayItemScraper()
        self.AmazonItemScraper = AmazonItemScraper()
        self.EbaySearchResultsScraper = EbaySearchResultsScraper()
        self.AmazonSearchResultsScraper = AmazonSearchResultsScraper()

    ## Function to determine if the URL passed in is for the Ebay platform
    # @param URL The web page to analyze
    # @return True if the URL is an Ebay link, False otherwise
    def isEbayURL(self, URL):
        if "ebay.com" in URL:
            return True
        return False

    ## Function to determine if the URL passed in is for the Amazon platform
    # @param URL The web page to analyze
    # @return True if the URL is an Amazon link, False otherwise
    def isAmazonURL(self, URL):
        if "amazon.com" in URL:
            return True
        return False

    ## Function to set the Ebay URL for the specific scraper object
    # @param url The URL associating a web page to the Ebay scraper
    def setEbayItemPageURL(self, URL):
        self.EbayItemScraper.setURL(URL)

    ## Function to set the Amazon URL for the specific scraper object
    # @param url The URL associating a web page to the Amazon scraper
    def setAmazonItemPageURL(self, URL):
        self.AmazonItemScraper.setURL(URL)

    ## Function to set the Ebay URL for the specific search result scraper object
    # @param url The URL associating a web page to the Ebay scraper
    def setEbaySearchResultsPageURL(self, URL):
        self.EbaySearchResultsScraper.setURL(URL)

    ## Function to set the Amazon URL for the specific search result scraper object
    # @param url The URL associating a web page to the Amazon scraper
    def setAmazonSearchResultsPageURL(self, URL):
        self.AmazonSearchResultsScraper.setURL(URL)

    ## Interface call to scrape the Ebay web page defined in the scraper's URL
    # @return A tuple containing the scraped name, buyout price, bid price and auction time remaining
    def scrapeEbayItemPage(self):
        (name, buyout, bid, time) = self.EbayItemScraper.scrapeEbayLink()
        return name, buyout, bid, time

    ## Interface call to scrape the Amazon web page defined in the scraper's URL
    # @return A tuple containing the scraped name, buyout price, bid price and auction time remaining
    #         NOTE: Since Amazon doesn't support auctions, we will default the bid price and time remaining to
    #               NA in this tuple
    def scrapeAmazonItemPage(self):
        (name, price) = self.AmazonItemScraper.scrapeAmazonLink()
        return name, price, "NA", "NA"