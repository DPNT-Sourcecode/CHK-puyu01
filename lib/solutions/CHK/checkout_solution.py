

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus is not None:
        skus = skus.upper()
    
    if not skus:
        return -1
    
    #Validate if all characters are valid SKUs
    if not all(item in 'ABCD' for item in skus):
        return -1

    # Global Variables
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    # Special Offers
    special_offers = {
        'A': (3, 130),
        'B': (2, 45),
    }
    
    # Count the number of ocurrences of each item
    item_counts = {}
    for item in skus:
        item_counts[item] = item_counts.get(item, 0) + 1
        
    total = 0
    
    # Calculate the total price considering special offers
    for item, count in item_counts.items():
        if item in special_offers:
            offer_count, offer_price = special_offers[item]
            total += (count // offer_count) * offer_price
            total += (count % offer_count) * prices[item]
        else:
            total += count * prices[item]
    return total
