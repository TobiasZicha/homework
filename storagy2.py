products = [
    {"name": "Audi", "price": 50},
    {"name": "BMW", "price": 30},
    {"name": "Audi A7", "price": 20},
    {"name": "Audi A8", "price": 20}
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


def average_price():
    if not products:
        print("No products available.")
        return

    average = 0
    count = 0

    for product in products:
        average += product["price"]
        count += 1

    avg_price = average / count

    print(f"Average product price: {avg_price:.2f}$")

def edit_product():
    print("\nSeznam produktů k úpravě:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product['name']} - {product['price']}$")

    try:
        index = int(input("\nZadejte číslo produktu, který chcete upravit: ")) - 1
        if index < 0 or index >= len(products):
            print("Neplatná volba. Zkuste to znovu.")
            return

        new_name = input("Zadejte nový název produktu: ")
        if not new_name:
            print("Název nesmí být prázdný.")
            return

        while True:
            try:
                new_price = float(input("Zadejte novou cenu produktu: "))
                new_price = int(new_price) if new_price.is_integer() else new_price
                break
            except ValueError:
                print("Neplatné číslo. Zadejte prosím platnou cenu.")

        products[index]["name"] = new_name
        products[index]["price"] = new_price
        print(f"\n Produkt byl úspěšně upraven: {new_name} - {new_price}$")

    except ValueError:
        print("Neplatná volba. Musíte zadat číslo.")



def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání produktu")
    print("4. Celková cena")
    print("5. Nejdražší produkt")
    print("6. Nejlevně produkt")
    print("7. Průměrná cena")
    print("8. Úprava produktu\n")

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
        print("Celková cena:")
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

    elif choice == 7:
        print("průměrná cena")
        average_price()
        print("\n")
        menu()

    elif choice == 8:
        print("změna ceny a názvu produktu")
        edit_product()
        print("\n")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
