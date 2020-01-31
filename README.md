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

## Running the system
Simply run the command *python IntelligentScraper.py* to start the system. The system will prompt you to enter a command. The following are the current supportedd commands:
- *store_item* - Scrape a single item web page, display item metadata and store the information 
- *store_items* – Scrape a search results web page, display item metadata and store the information
- *update* – Updates the current contents of the database and alerts the user upon price change
- *display* – Displays the current contents of the database to the user
- *export* – Dump the internal database tracking all of the user queried items to a spreadsheet and exit the tool
- *exit* – Exit the tool and return control to the user

## Supported Platforms
- Amazon
- Ebay
