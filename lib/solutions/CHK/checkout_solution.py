# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    if not skus:
        return 0
    
    # Validate if all characters are valid SKUs
    if not all(item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for item in skus):
        return -1

    # Global Variables
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
        'Y': 20, 'Z': 21
    }

    # Special Multi-Price Offers
    special_multiprice_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)],
    }
    
    # Group Discount Items
    group_discount_items = ['S', 'T', 'X', 'Y', 'Z']
    group_discount_size = 3
    group_discount_price = 45
    
    # Count the number of occurrences of each item
    item_counts = {}
    for item in skus:
        item_counts[item] = item_counts.get(item, 0) + 1
        
    # Process Group Discounts
    group_discount_count = 0
    group_items_prices = []
    
    # Collect items eligible for group discount
    for item in group_discount_items:
        if item in item_counts:
            count = item_counts[item]
            group_items_count += count
            # add ech item price to list repeated by count
            group_items_prices.extended([prices[item]] * count)
            
    # Apply group discounts
    group_discount_count = group_items_count // group_discount_size
    remaining_group_items = group_items_count % group_discount_size
    
    # calculate how many of ech group item to remove after the discount
    if group_discount_count > 0:
        items_to_remove = group_discount_count * group_discount_size
        
    # Calculate item count after group discount
    for item in group_discount_items:
        if item in item_counts and items_to_remove > 0:
            remove_count = min(item_counts[item], items_to_remove)
            item_counts[item] -= remove_count
            items_to_remove -= remove_count
            if item_counts[item] == 0:
                del item_counts[item]
        
    # Process "get free item" offers
    
    # 2E get one B free 
    if 'E' in item_counts and 'B' in item_counts:
        free_b_count = item_counts['E'] // 2
        item_counts['B'] = max(0, item_counts['B'] - free_b_count)
        
    # 2F get one F free
    if 'F' in item_counts:
        free_f_count = item_counts['F'] // 3
        item_counts['F'] -= free_f_count
        
    # 3N get one M free
    if 'N' in item_counts and 'M' in item_counts:
        free_m_count = item_counts['N'] // 3
        item_counts['M'] = max(0, item_counts['M'] - free_m_count)
        
    # 3R get one Q free
    if 'R' in item_counts and 'Q' in item_counts:
        free_q_count = item_counts['R'] // 3
        item_counts['Q'] = max(0, item_counts['Q'] - free_q_count)
        
    # 3U get one U free
    if 'U' in item_counts:
        free_u_count = item_counts['U'] // 4
        item_counts['U'] -= free_u_count
        
    total = 0
    
    # group discount total
    total += group_discount_count * group_discount_price
    
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