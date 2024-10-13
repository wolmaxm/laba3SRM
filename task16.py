
def calculation(pricelist, order):
    total_cost = 0  

    pricelist = [(item[0].strip().lower(), item[1], item[2]) for item in pricelist]

    for item, quantity in order:
        item_cleaned = item.strip().lower() 
       
        matched_item = next((p for p in pricelist if p[0] == item_cleaned), None)

        if not matched_item:
            return -2  

        price, available = matched_item[1], matched_item[2]  

        if quantity > available:
            return -1  

        total_cost += price * quantity  

        
        for i in range(len(pricelist)):
            if pricelist[i][0].strip().lower() == item_cleaned:
                temp_item = list(pricelist[i])
                temp_item[2] -= quantity  
                pricelist[i] = tuple(temp_item)  

    return total_cost, pricelist  

pricelist = [
    ['Хліб', 25, 10],
    ['Молоко', 20, 5],
    ['Яблуко', 15, 10]
]
order = [
    ('хліб', 2),
    ('Молоко', 3),
    ('Яблуко', 5)
]

order_cost = calculation(pricelist, order)
print(order_cost)


