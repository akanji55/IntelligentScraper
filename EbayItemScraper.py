from BaseScraper import BaseScraper # Used to import the base class to inherit from
from bs4 import BeautifulSoup # Used to parse an html web page
import requests # Used to get an html page given a URL

# @brief Ebay scraper class used to scrape specific item web pages
class EbayItemScraper(BaseScraper):

    ## Initialize the Ebay Item Scraper object
    def __init__(self):
        super().__init__("EbayItemScraper") # Inherit from the base class

    ## Function to scrape an Ebay URL and return metadata information about the item
    # @return A tuple containing the following items:
    #         - Item Name
    #         - Buyout Price (if one exists)
    #         - Current Bid Price (if one exists)
    #         - Remaining Auction Time (if one exists)
    # NOTE: Try/Except blocks used to protect against missing html elements
    def scrapeEbayLink(self):
        itemName = "NA"  # Default name to NA when can't infer name
        buyoutPrice = "NA"  # Default buyout to NA when can't infer buyout price
        bidPrice = "NA"  # Default bid to NA when can't infer bid price
        remainingTime = "NA" # Default time to NA when can't infer remaining auction time
        getInfo = requests.get(self.URL)
        util = BeautifulSoup(getInfo.text, 'html.parser')
        try:
            itemName = util.find("h1", {"id": "itemTitle"}).get_text()
            itemName = self.convertEbayItemString(itemName)
        except: # Can't find the item name on the web page
            print("Could not infer item from Ebay page")
        buyoutPrices = util.find_all(id="prcIsum")
        bidPrices = util.find_all(id="prcIsum_bidPrice")
        if len(buyoutPrices) == 0 and len(bidPrices) == 0:
            print("Could not find any price information for this item")
        else:
            if len(buyoutPrices) == 1:
                buyoutPrice = buyoutPrices[0].get_text().strip()
            if len(bidPrices) == 1:
                bidPrice = bidPrices[0].get_text().strip()
                try:
                    remainingTime = util.find("span", {"id": "vi-cdown_timeLeft"}).get_text().strip()
                except: # Can't find the remaining auction time on the web page
                    print("Could not infer remaining time for this auction")
        return itemName, buyoutPrice, bidPrice, remainingTime

    ## Function to clean the item name of all miscelaneous characters from an item name
    # @param itemTitle The string for the item title extracted from an Ebay web page
    # @return The title of the item with the unnecessary characters removed
    def convertEbayItemString(self, itemTitle):
        newItem = itemTitle[15:].strip()
        return newItem

