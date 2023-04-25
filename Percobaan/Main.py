import tkinter as tk
import requests

class CurrencyConverter:
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != "IDR":
            amount = amount / self.rates[from_currency]

        amount = round(amount * self.rates[to_currency], 2)
        return amount

class CurrencyConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        self.converter = CurrencyConverter("https://api.exchangerate-api.com/v4/latest/IDR")

        # create the widgets
        self.from_label = tk.Label(self.master, text="From Currency:")
        self.from_label.grid(row=0, column=0, padx=5, pady=5)

        self.from_currency = tk.StringVar()
        self.from_currency.set("IDR")
        self.from_dropdown = tk.OptionMenu(self.master, self.from_currency, *self.converter.rates.keys())
        self.from_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = tk.Label(self.master, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.to_label = tk.Label(self.master, text="To Currency:")
        self.to_label.grid(row=2, column=0, padx=5, pady=5)

        self.to_currency = tk.StringVar()
        self.to_currency.set("EUR")
        self.to_dropdown = tk.OptionMenu(self.master, self.to_currency, *self.converter.rates.keys())
        self.to_dropdown.grid(row=2, column=1, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=3, column=1, padx=5, pady=5)

        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert)
        self.convert_button.grid(row=4, column=1, padx=5, pady=5)

    def convert(self):
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        amount = float(self.amount_entry.get())

        converted_amount = self.converter.convert(from_currency, to_currency, amount)

        result_text = f"{amount} {from_currency} = {converted_amount} {to_currency}"
        self.result_label.config(text=result_text)

# create the application window
root = tk.Tk()
currency_converter_gui = CurrencyConverterGUI(root)
root.mainloop()
