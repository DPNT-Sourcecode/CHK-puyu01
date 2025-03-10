# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    if not skus:
        return 0
    
    # Validate if all characters are valid SKUs
    if not all(item in "ABCDEF" for item in skus):  # Re-typed with quotes
        return -1

    # Global Variables
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
    }

    # Special Multi-Price Offers
    special_multiprice_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)]
    }
    
    # Count the number of occurrences of each item
    item_counts = {}
    for item in skus:
        item_counts[item] = item_counts.get(item, 0) + 1
        
    # Process "get free item" offers first
    if 'E' in item_counts and 'B' in item_counts:
        free_b_count = item_counts['E'] // 2
        item_counts['B'] = max(0, item_counts['B'] - free_b_count)
        
    #2F get one F free
    if 'F' in item_counts:
        free_f_count = item_counts['F'] // 3
        item_counts['F'] -= free_f_count
        
    total = 0
    
    # Calculate the total price considering special offers
    for item, count in item_counts.items():
        if item in special_multiprice_offers:
            remaining_count = count
            for offer_qty, offer_price in special_multiprice_offers[item]:
                offer_count = remaining_count // offer_qty
                total += offer_count * offer_price
                remaining_count %= offer_qty
            total += remaining_count * prices[item]
        else:
            total += count * prices[item]
    
    return total
