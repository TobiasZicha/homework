products = [
    {"name": "Audi", "price": 50},
    {"name": "BMW", "price": 30},
    {"name": "Audi ahoj", "price": 20},
    {"name": "Audi blbec", "price": 20}
]


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}$")

#funkce search product - vyhledávání produktu
def search_product():
    query = input("Zadejte hledaný název produktu: ").lower()
    results = []

    for product in products:
        if query in product["name"].lower():
            results.append(product)

    if results:
        print("Nalezené produkty:")
        for item in results:
            print(f"{item['name']} - {item['price']}$")
    else:
        print("Žádný produkt nenalezen.")

#cena vsech produktu dohromady
def total_price():
    total = 0

    for product in products:
        total += product["price"]

    print(f"Celková cena všech produktů je: {total}$")


def add_product():
    product_name = input("Název produktu:")

    while True:
        try:
            product_price = float(input("Cena produktu:  "))
            break
        except ValueError:
            print("Neplatné číslo")

    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)
    print("Produkt úspěšně přidán")


def array_min(items):
    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item

def cheapest_product():

    min_price = array_min([product["price"] for product in products])
    cheapest = [product for product in products if product["price"] == min_price]

    print("Nejlevnější produkt:")
    for product in cheapest:
        print(f"{product['name']} - {product['price']}$")

def array_max(items):
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

def most_expensive_product():

    max_price = array_max([product["price"] for product in products])
    most_expensive = [product for product in products if product["price"] == max_price]

    print("Nejdražší produkt:")
    for product in most_expensive:
        print(f"{product['name']} - {product['price']}$")



def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání produktu")
    print("4. suma produktu")
    print("5. Nejdražší produkt")
    print("6. Nejlevně produkt\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání poožky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("vyhledání produktu:")
        search_product()
        print("")
        menu()

    elif choice == 4:
        print("suma produktu:")
        total_price()
        print("")
        menu()

    elif choice == 5:
        print("Nejdražší produkt:")
        most_expensive_product()
        print("")
        menu()

    elif choice == 6:
        print("Nejlevnější produkt:")
        cheapest_product()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
