# Map con diccionarios

items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'polo',
        'price': 50
    }
]

# Transformar esto a que solo me devuelva una lista con solo de los precios

prices = list(map(lambda item: item['price'], items))
print(prices)

# Agregar atributos nuevo a cada diccionarios, modificamos todo el array original si no copiamos
# el array original.

def add_taxes(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .19
    return new_item

new_items = list(map(add_taxes, items))
print("New Array")
print(new_items)
print("Old Array")
print(items)



