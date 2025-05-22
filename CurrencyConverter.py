import requests
API_KEY = "be7dc9cd742acb99ab737dee"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def GetExchangeRates(base_currency):
    """Return a dict of rates for the given base currency (or None on error)."""
    response = requests.get(BASE_URL + base_currency.upper())
    data = response.json()
    return data["conversion_rates"] if data.get("result") == "success" else None

def ConvertCurrency(amount, from_currency, to_currency, rates):
    """Convert amount using the rates dict."""
    if to_currency.upper() in rates:
        return amount * rates[to_currency.upper()]
    else:
        print(f"Error: '{to_currency}' not found in rate table.")
        return None

print("*" * 10, "Currency Converter", "*" * 10)

while True:
    print("\n1. Convert Currency\n2. Exit")
    choice = int(input("Enter Your Choice (1-2): "))

    if choice == 1:
        base = input("Enter base currency code (e.g., USD): ").upper()
        target = input("Enter target currency code (e.g., INR): ").upper()
        try:
            amount = float(input(f"Enter amount in {base}: "))
        except ValueError:
            print("Invalid amount!")
            continue

        rates = GetExchangeRates(base)
        if rates:
            result = ConvertCurrency(amount, base, target, rates)
            if result is not None:
                print(f"{amount:.2f} {base} = {result:.2f} {target}")
        else:
            print("Error fetching exchange rates. Check API key or currency code.")
    elif choice == 2:
        print("Thank You!!")
        break
    else:
        print("Invalid Choice!!!!\nPlease Enter Correct choice")
