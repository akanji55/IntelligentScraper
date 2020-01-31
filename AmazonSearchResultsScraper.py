from BaseScraper import BaseScraper # Used to import the base class to inherit from
from bs4 import BeautifulSoup # Used to parse an html web page
import requests # Used to get an html page given a URL
import lxml # Used to parse the Amazon web page

# @brief Amazon scraper class used to scrape a search results page for multiple items on Amazon
class AmazonSearchResultsScraper(BaseScraper):

    ## Initialize the Amazon Search Results Scraper object
    def __init__(self):
        super().__init__("AmazonSearchResultsScraper") # Inherit from the base class