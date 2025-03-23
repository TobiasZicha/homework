# Správa skladových produktů

Tento projekt je jednoduchá konzolová aplikace napsaná v jazyce Python, která umožňuje správu produktů na skladě. Umožňuje přidávat, upravovat, hledat produkty, zjistit jejich celkovou cenu, nejdražší a nejlevnější produkt, průměrnou cenu, poslední přidaný produkt a ukončit program.

## Funkce aplikace

Aplikace obsahuje několik hlavních funkcí:

1. **Výpis položek** – Vypíše všechny produkty na skladě.
2. **Přidání položky** – Umožňuje přidat nový produkt.
3. **Vyhledání produktu** – Hledá produkt dle jména.
4. **Celková cena** – Spočítá celkovou cenu všech produktů.
5. **Nejdražší produkt** – Najde a zobrazí nejdražší produkt.
6. **Nejlevnější produkt** – Najde a zobrazí nejlevnější produkt.
7. **Průměrná cena** – Spočítá průměrnou cenu produktů.
8. **Úprava produktu** – Umožňuje upravit produkt.
9. **Zobrazení posledního přidaného produktu** - Zobrazí produkt, který byl posledně přidán.
10. **Ukončení programu** – Umožňuje bezpečně ukončit program.

## Popis funkcí v kódu - Velmi podrobně rozebraný

### `add_product()`
Funkce přidá nový produkt do seznamu `products`. Uživatel zadá nazev a cenu produktu. Cena je validována pomocí cyklu `while`, který kontroluje, zda uživatel zadal platné číslo. Pokud zadá neplatný vstup, zobrazí se chybová zpráva a proces se opakuje, dokud není zadána správná hodnota.

### `array_min(items)`
Tato funkce implementuje vlastní způsob nalezení minimální hodnoty v seznamu, protože funkce `min` není povolena. Prochází seznam položek a ukládá nejmenší nalezenou hodnotu do proměnné `min_item`, kterou na konci vrátí. Používá se v `cheapest_product()`.


### `cheapest_product()`
Funkce používá `array_min()` k nalezeni nejnižší ceny mezi produkty. Poté projde seznam `products` a všechny produkty s touto cenou vypíše. Pokud existuje více produktů se stejnou nejnižší cenou, zobrazi se všechny.


### `array_max(items)`
Podobně jako `array_min()`, tato funkce implementuje vlastní způsob nalezení maximální hodnoty v seznamu. Používá proměnnou `max_item` k uchování největší hodnoty, kterou na konci vrátí. Používá se v `most_expensive_product()`.

### `most_expensive_product()`
Tato funkce používá `array_max()` k nalezení nejvyšší ceny mezi produkty. Poté projde seznam `products` a vypíše všechny produkty, které mají tuto cenu. Stejně jako u `cheapest_product()`, pokud existuje více produktů se stejnou maximální cenou, zobrazí se všechny.


### `average_price()`
Funkce vypočítá průměrnou cenu všech produktů v seznamu `products`. Pokud seznam neobsahuje žádné produkty, zobrazí se zpráva o jejich nedostupnosti a funkce se ukončí. Jinak projde všechny produkty, sečte jejich ceny a vydělí jejich počet, čímž získá průměr. Výsledek je formátován na dvě desetinná místa.

### `edit_product()`
Funkce umožňuje uživateli upravit existující produkt v seznamu. Nejprve vypíše všechny dostupné produkty s číslováním. Uživatel zadá číslo produktu, který chce upravit. Pokud zadá neplatné číslo, zobrazí se chybová zpráva. Poté může změnit název produktu a cenu. Název nesmí být prázdný a cena musí být platné číslo. Pokud uživatel zadá cenu jako celé číslo, je převedena na `int`, jinak zůstane `float`. Na konci se zobrazí potvrzení o úspěšné úpravě.

### `end()`
Funkce zkontroluje, zda uživatel zadal číslo `9`. Pokud ano, zobrazí zprávu o ukončení programu a ukončí běh aplikace pomocí `quit()`. Jinak umožní pokračovat v programu.

### `menu()`
Tahle funkce zajišťuje hlavní ovládání programu. Zobrazí uživateli menu s číslovanými možnostmi a čeká na vstup. Pokud uživatel zadá neplatnou volbu, zobrazí se chybová zpráva a menu se zobrazí znovu. Podle vybrané možnosti volá odpovídající funkci. Program běží v nekonečné smyčce `while True`, dokud uživatel nezvolí ukončení.

### `latest_added_product`
Tahle funkce zjišťuje a zobrazuje poslední přidaný produkt ve tvém seznamu products. Pokud je seznam prázdný, funkce vypíše zprávu „Žádné produkty nejsou v skladu“ a ukončí svou činnost. Pokud seznam produktů není prázdný, funkce získá poslední přidaný produkt tím, že se podívá na poslední položku v seznamu products. Nakonec funkce vytiskne informace o posledním přidaném produktu, tedy jeho název a cenu.

## Co mi pomohlo při dělání projektu

* W3Schools 

* Chat gpt

* Youtube

