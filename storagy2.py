products = [
    {"name": "Audi", "price": 50},
    {"name": "BMW", "price": 30},
    {"name": "Audi A8", "price": 20},
    {"name": "Audi A7", "price": 20}
]


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}$")


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


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání produktu\n")


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

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
