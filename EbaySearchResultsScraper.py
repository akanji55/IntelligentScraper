from BaseScraper import BaseScraper # Used to import the base class to inherit from
from bs4 import BeautifulSoup # Used to parse an html web page
import requests # Used to get an html page given a URL

# @brief Ebay scraper class used to scrape a search results page for multiple items on Ebay
class EbaySearchResultsScraper(BaseScraper):

    ## Initialize the Ebay Search Results Scraper object
    def __init__(self):
        super().__init__("EbaySearchResultsScraper") # Inherit from the base class