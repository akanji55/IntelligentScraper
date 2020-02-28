from BaseScraper import BaseScraper # Used to import the base class to inherit from
from bs4 import BeautifulSoup # Used to parse an html web page
import requests # Used to get an html page given a URL
import lxml # Used to parse the Amazon web page

# @brief Amazon scraper class used to scrape specific item web pages
class AmazonItemScraper(BaseScraper):

    ## Initialize the Amazon Item Scraper object
    def __init__(self):
        super().__init__("AmazonItemScraper") # Inherit from the base class

    ## Function to scrape an Amazon URL and return metadata information about the item
    # @return A tuple containing the following items:
    #         - Item Name
    #         - Price
    # NOTE: Try/Except blocks used to protect against missing html elements
    def scrapeAmazonLink(self):
        itemName = "NA"  # Default name to NA when can't infer name
        price = "NA"  # Default price to NA when can't infer buyout price

        # NOTE: Due to Amazon trying to prevent bots from scraping their web pages,
        # specific headers will need to be used in order to request properly. These headers
        # may need to change at times to support emulating an actual browser GET request.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'}

        newHeaders = {'User-Agent':
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/54.0.2840.71 Safari/537.36'}

        getInfo = requests.get(self.URL, headers=newHeaders)
        util = BeautifulSoup(getInfo.content, features="lxml")
        try:
            itemName = util.find("span", {"id": "productTitle"}).get_text().strip()
        except: # Can't find the item name on the web page
            print("Could not infer item from Amazon page")
        prices = util.find_all(id="priceblock_ourprice")
        if len(prices) == 1:
            price = prices[0].get_text().strip()
        else:
            print("There is no price for this item")
        return itemName, price