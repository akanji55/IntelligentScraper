# @brief Base class for all of our unique scrapers to inherit from
class BaseScraper:

    ## Initialize the base class object
    # @param name The name of the scraper object to create
    def __init__(self, name):
        self.name = name
        self.URL = ""

    ## Function to set the URL to scrape
    # @param url The URL associating a web page to the scraper
    def setURL(self, url):
        self.URL = url