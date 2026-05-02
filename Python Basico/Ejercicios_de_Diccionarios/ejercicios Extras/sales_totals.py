products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]


totals_group = {}

for product in products:     
    totals = product['price']
    cat = product['category'] 
    
    if cat not in totals_group:
        totals_group[cat] = 0
    
    totals_group[cat] += totals   

print(totals_group)