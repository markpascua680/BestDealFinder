
# Returns all items on first results page on a website
def getData(all_items, all_prices):

    # Pick out each product's individual name and price from HTML
        items = []
        prices = []
        for item in all_items:
            items.append(item.string)
    
        for price in all_prices:
            prices.append(price.string)
    
        # Pair product names and prices in a tuple
        items_and_prices = [()]
        for i in range(len(items)):
            items_and_prices.append((items[i], prices[i]))
            
        # Print products and their prices
        for item in items_and_prices:
            result = ': '.join(item)
            print(result + '\n')        # TEMPORARY PRINT STATEMENT