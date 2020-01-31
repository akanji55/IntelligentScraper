from ScraperLibrary import ScraperLibrary # Import the library class that contains all the scrapers
from ItemDatabase import ItemDatabase # Import the database class to maintain all tracked items
import threading

# @brief System class to act as our delivered functional system
class IntelligentScraper:

    ## Initialize the Scraper Library object
    def __init__(self):
        self.name = "IntelligentScraper"
        self.library = ScraperLibrary()
        self.database = ItemDatabase()
        self.timer = threading.Timer(60.0, self.updateDatabase)

    ## Function to update the database with the most up to date prices
    ## This function is ran on a separate thread and will be triggered once every minute
    def updateDatabase(self):
        print("THREADING IS WORKING")
        self.timer = threading.Timer(60.0, self.updateDatabase)
        self.timer.start()

    ## Function to accept user input, store information and display status to the user
    ## This function will loop forever until the user decides to exit the tool
    def invoke(self):
        print("Welcome to the Intelligent Scraper Tool!")
        print("The following commands are supported by the tool")
        print("store_item - Scrape an Ebay/Amazon single item web page, display item metadata and store the information")
        print("store_items - Scrape an Ebay/Amazon search results web page, "
              "display item metadata for each item and store the information")
        print("display - Displays the items being tracked and associated metadata in the internal database")
        print("update - Updates the database with the most up to date information")
        print("export - Dump the internal database tracking all items to a spreadsheet and exit the tool")
        print("exit - Exit the tool")
        self.timer.start()  # Start the timer thread to periodically update the database
        userInput = ""

        # Continuously loop until the user wants to exit the tool.
        # The user can exit by either typing "exit" to stop the tool from running or
        # "export" which will output a spreadsheet of the current database before exiting the tool
        while userInput is not "exit":
            userInput = input("Please enter a supported command: ")
            if userInput == "exit": # Quit the tool option
                print("Thank you for using the Intelligent Scraper Tool!")
                self.timer.cancel()
                return
            elif userInput == "export": # Export spreadsheet and quit option
                self.database.exportTrackedItems()
                print("Thank you for using the Intelligent Scraper Tool! Your spreadsheet has been generated.")
                self.timer.cancel()
                return
            elif userInput == "store_item":
                url = input("Please enter an Ebay/Amazon single item URL: ")
                if self.library.isEbayURL(url): # Scrape an Ebay page option
                    self.library.setEbayItemPageURL(url) # Set the URL
                    (name, buyout, bid, time) = self.library.scrapeEbayItemPage() # Scrape page for relevant data
                    self.database.addEntry(url, "ebay", name, buyout, bid, time) # Store data and print results
                elif self.library.isAmazonURL(url): # Scrape an Amazon page option
                    self.library.setAmazonItemPageURL(url) # Set the URL
                    (name, buyout, bid, time) = self.library.scrapeAmazonItemPage() # Scrape page for relevant data
                    self.database.addEntry(url, "amazon", name, buyout, bid, time)  # Store data and print results
                else:
                    print("Inputted URL for platform not currently supported")
            elif userInput == "store_items":
                url = input("Please enter an Ebay/Amazon search results URL: ")
                if self.library.isEbayURL(url):  # Scrape an Ebay page option
                    self.library.setEbaySearchResultsPageURL(url)  # Set the URL
                    ## Placeholder to scrape Ebay Search Results page and store in database
                elif self.library.isAmazonURL(url):  # Scrape an Amazon page option
                    self.library.setAmazonSearchResultsPageURL(url)  # Set the URL
                    ## Placeholder to scrape Amazon Search Results page and store in database
                else:
                    print("Inputted URL for platform not currently supported")
            elif userInput == "update":
                print("Placeholder for update functionality")
            elif userInput == "display":
                self.database.display()
            else:
                print("Invalid entry found! Please follow the prompted guidelines for acceptable input")

## Run the main function when the python script is called
if __name__ == "__main__":
    scraper = IntelligentScraper()
    scraper.invoke()