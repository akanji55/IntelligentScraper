import xlsxwriter # Import to export database to spreadsheet
import re
from datetime import datetime

# @brief Database class to maintain all of the URL items the user has scraped for
class ItemDatabase:

    ## Initialize the Item Database object
    def __init__(self):
        self.name = "ItemDatabase"
        self.database = {} # Database is set as a dictionary of list of lists to support multiple items for one URL

    ## Function to add a scraped item to the dictionary database
    # @param URL The web page which will be the key to the database
    # @param platform The platform that the URL relates to
    # @param itemName The name of the item extracted from the scraped page
    # @param buyoutPrice The buyout price of the item
    # @param bidPrice The bid price of the item
    # @param remainingTime The remaining time that the item is listed for
    def addEntry(self, URL, platform, itemName, buyoutPrice, bidPrice, remainingTime):
        print("\n")
        print("Item: " + itemName)
        print("Buyout Price: " + buyoutPrice)
        print("Current Bid Price: " + bidPrice)
        print("Remaining Auction Time: " + remainingTime)
        print("\n")
        timestamp = datetime.now()
        self.database[URL] = [[platform, itemName, buyoutPrice, bidPrice, remainingTime, str(timestamp)]]

    ## Function to update an items entry in the dictionary database
    # @param URL The web page which will be the key to the database
    # @param platform The platform that the URL relates to
    # @param itemName The name of the item extracted from the scraped page
    # @param buyoutPrice The buyout price of the item
    # @param bidPrice The bid price of the item
    # @param remainingTime The remaining time that the item is listed for
    def updateEntry(self, URL, platform, itemName, buyoutPrice, bidPrice, remainingTime):
        currentItem = self.database[URL]
        if currentItem is None:
            return

        ## Compare the buyout price to see if there is a price change
        # If the old price is NA and new price is not, assume price change
        if currentItem[2] == "NA" and buyoutPrice != "NA":
            print("ALERT: There has been a buyout price change for " + itemName + " on " + platform +
                  ". Old buyout price: NA. New buyout price: " + buyoutPrice)

        # If both of the items are not NA, assume they have a price and check for update
        elif currentItem[2] != "NA" and buyoutPrice != "NA":
            oldBuyoutPrice = self.convertPriceToFloat(currentItem[2])
            newBuyoutPrice = self.convertPriceToFloat(buyoutPrice)
            if oldBuyoutPrice != newBuyoutPrice:
                print("ALERT: There has been a buyout price change for " + itemName + " on " + platform +
                      ". Old buyout price: " + currentItem[2] + ". New buyout price: " + buyoutPrice)

        ## Compare the bid price to see if there is a price change
        # If the old price is NA and new price is not, assume price change
        if currentItem[3] == "NA" and bidPrice != "NA":
            print("ALERT: There has been a bid price change for " + itemName + " on " + platform +
                  ". Old bid price: NA. New bid price: " + bidPrice)

        # If both of the items are not NA, assume they have a price and check for update
        elif currentItem[3] != "NA" and bidPrice != "NA":
            oldBidPrice = self.convertPriceToFloat(currentItem[3])
            newBidPrice = self.convertPriceToFloat(bidPrice)
            if oldBidPrice != newBidPrice:
                print("ALERT: There has been a bid price change for " + itemName + " on " + platform +
                      ". Old bid price: " + currentItem[3] + ". New bid price: " + bidPrice)

        # Now that the user has been notified if a price change has occurred, update the internal entry
        timestamp = datetime.now()
        self.database[URL] = [[platform, itemName, buyoutPrice, bidPrice, remainingTime, str(timestamp)]]

    ## Function to display the current contents of the database
    def display(self):
        print("{:<15} {:<15} {:<15} {:<20} {:<50} {:<100}"
              .format('Platform', 'Buyout Price', 'Bid Price', 'Auction Time', 'Timestamp', 'Item Name'))
        for key in self.database.keys():
            for entry in self.database[key]:
                print("{:<15} {:<15} {:<15} {:<20} {:<50} {:<100}"
                      .format(entry[0], entry[2], entry[3], entry[4], entry[5], entry[1]))
        print("\n")

    ## Function to trasnfer the database to a spreadsheet and output it to the user
    def exportTrackedItems(self):
        headers = ['URL', 'Platform', 'Item', 'Buyout Price', 'Bid Price', 'Auction Time Remaining', 'Timestamp']
        counter = 0

        # Create spreadsheet and create rules that will be used to format cells
        workbook = xlsxwriter.Workbook('TrackedItems.xlsx')
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        wrap = workbook.add_format()
        wrap.set_text_wrap()
        worksheet.set_column(0, 0, 100, wrap)
        worksheet.set_column(1, 1, 30, wrap)
        worksheet.set_column(2, 2, 60, wrap)
        worksheet.set_column(3, 3, 30, wrap)
        worksheet.set_column(4, 4, 30, wrap)
        worksheet.set_column(5, 5, 30, wrap)
        worksheet.set_column(6, 6, 30, wrap)

        # Populate spreadsheet with headers
        for counter, h in enumerate(headers):
            worksheet.write(0, counter, h, bold)
            counter += 1

        # Add database dictionary to the spreadsheet
        row = 1
        col = 0
        for key in self.database.keys():
            for entry in self.database[key]:
                worksheet.write(row, col, key)
                i = 1
                for item in entry:
                    worksheet.write(row, col + i, item)
                    i += 1
                row += 1
        workbook.close() # Output the spreadsheet

    ## Function to clean a price string and convert it to a float
    # @param priceStr The price string to clean and convert
    # @return the floating point value of the price
    def convertPriceToFloat(self, priceStr):
        clean = re.compile(r'[^\d.,]+')
        result = clean.sub('', priceStr)
        return float(result.replace(',',''))

    ## Function to get all of the items in the database that we want to update
    ## Note that we will only update an entry if the association is one to one for URL to items.
    # @return The list of all of the urls to update
    def getItemsToUpdate(self):
        items = []
        for key in self.database.keys():
            if len(self.database[key]) == 1:
                items.append(key)
        return items
