# IntelligentScraper

## Required Libraries
- Python 3.6
- XlsxWriter
- beautifulsoup4
- lvml
- requests
- urllib3
- re
- threading
- datetime

## Installing Required Libraries
Installing the required libraries can be done using the *pip install* command. For example, to install the XlsxWriter library, you would run the following command *pip install XlsxWriter*.

## Running the system
Simply run the command *python IntelligentScraper.py* to start the system. The system will prompt you to enter a command. The following are the current supported commands:
- *store_item* - Scrape a single item web page, display item metadata and store the information 
- *store_items* – Scrape a search results web page, display item metadata and store the information
- *update* – Updates the current contents of the database and alerts the user upon price change
- *display* – Displays the current contents of the database to the user
- *export* – Dump the internal database tracking all of the user queried items to a spreadsheet and exit the tool
- *exit* – Exit the tool and return control to the user

Upon entering a supported command, the system will prompt the user for specific information depending on the information passed in.

## Supported Platforms
- Amazon
- Ebay
