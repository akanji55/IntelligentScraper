# IntelligentScraper

## Repository Location
All of the code for the Intelligent Scraper system exists on github. This repository can be found at the following URL: https://github.com/akanji55/IntelligentScraper

## Cloning Reporitory
In order to run the Intelligent Scraper system, the above repository will need to be cloned to your local machine. This can be done by utilizing the *Clone or download* feature found on github. Some IDEs have functionality built in that allow the user to clone a repository from with the environment. You will also need the following required libraries:
- Python 3.6
- XlsxWriter
- beautifulsoup4
- lxml
- requests
- urllib3
- re
- threading
- datetime

## Installing Required Libraries
Installing the required libraries can be done using the *pip install* command. For example, to install the XlsxWriter library, you would run the following command *pip install XlsxWriter*. This will need to be done for any of the required libraries that is not downloaded on the machine where Intelligent Scraper will be running.

## Running the system
To start the system simply run the command *python IntelligentScraper.py*. The system will prompt you to enter a command. The following are the current supported commands:
- *store_item* - Scrape a single item web page, display item metadata and store the information 
- *store_items* – Scrape a search results web page, display item metadata and store the information
- *update* – Updates the current contents of the database and alerts the user upon price change
- *display* – Displays the current contents of the database to the user
- *export* – Dump the internal database tracking all of the user queried items to a spreadsheet and exit the tool
- *exit* – Exit the tool and return control to the user

Upon entering a supported command, the system will prompt the user for specific information depending on the command passed in. For example, if the *store_item* command is sent to the system, the system will prompt the user to enter a URL for one of the supported platforms.

## Supported Platforms
Below are the currently supported website platforms that the system supports scraping of:
- Amazon
- Ebay
