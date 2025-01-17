# Utility App - Vending Machine
# Denise Marielle Menguita
# This program was made using the Tkinter tutorial by realpython.com as reference, as well as other tutorials.
# -------------------------------

import random #to randomize stock
import tkinter as tk #for graphical user interface (GUI) implementation
from tkinter import *
from tkinter import messagebox, ttk

#root/main GUI window
main = tk.Tk()

### START OF CODE MADE WITH HELP FROM TUTORIAL BY USER abhigoya ON GEEKSFORGEEKS. LINKED IN REFERENCE LIST ###
#change cursor
main.config(cursor="cross")
### END OF CODE MADE WITH HELP FROM TUTORIAL BY USER abhigoya ON GEEKSFORGEEKS. LINKED IN REFERENCE LIST ###

#nested dictionaries to store item categories, item names, price, and stock with randomized values
menu = {
    "Snacks": { #dictionary of snacks
        "A1": {
            "ID": "Lay's Classic",
            "price": 3.00, #prices taken from Lulu website
            "stock": random.randint(0, 5)}, ### MADE WITH HELP FROM TUTORIAL BY USER kartik ON GEEKSFORGEEKS. LINKED IN REFERENCE LIST ###
        "A2": {
            "ID": "Double Stuffed Oreo",
            "price": 3.00,
            "stock": random.randint(0, 5)}, #randomize stock between 0 and 5
        "A3": {
            "ID": "Oman Chips",
            "price": 3.50,
            "stock": random.randint(0, 5)},
        "A4": {
            "ID": "Cheetos Crunchy Cheese",
            "price": 2.50,
            "stock": random.randint(0, 5)},
    },
    "Chocolates": { #dictionary of chocolates
        "B1": {
            "ID": "Kit Kat",
            "price": 1.75,
            "stock": random.randint(0, 5)},
        "B2": {
            "ID": "Toblerone",
            "price": 3.75,
            "stock": random.randint(0, 5)},
        "B3": {
            "ID": "Snickers",
            "price": 3.00,
            "stock": random.randint(0, 5)},
        "B4": {
            "ID": "Ferrero Raffaello",
            "price": 4.30,
            "stock": random.randint(0, 5)},
    },
    "Drinks": { #dictionary of drinks
        "C1": {
            "ID": "Coca Cola",
            "price": 2.50,
            "stock": random.randint(0, 5)},
        "C2": {
            "ID": "Lacnor Mango",
            "price": 2.25,
            "stock": random.randint(0, 5)},
        "C3": {
            "ID": "Mountain Dew",
            "price": 2.35,
            "stock": random.randint(0, 5)},
        "C4": {
            "ID": "Water",
            "price": 1.00,
            "stock": random.randint(0, 5)},
    },
}

suggestions = {
    "Snickers": "Water",
    "Coca Cola": "Oman Chips",
    "Mountain Dew": "Lay's Classic",
    "Kit Kat": "Double Stuffed Oreo",
    "Ferrero Rocher": "Lacnor Mango",
    "Cheetos Crunchy Cheese": "Coca Cola",
    "Lay's Classic": "Mountain Dew",
    "Double Stuffed Oreo": "Snickers",
    "Toblerone": "Water",
    "Oman Chips": "Kit Kat",
    "Lacnor Mango": "Toblerone",
    "Water": "Ferrero Raffaello",
}

### START OF CODE MADE WITH HELP OF YOUTUBE TUTORIAL BY CHANNEL ATLAS. LINKED IN REFERENCE LIST ###
#style the GUI
style = ttk.Style()
style.configure("TLabel", font=("Jersey 10", 12))
### END OF CODE MADE WITH HELP OF YOUTUBE TUTORIAL BY CHANNEL ATLAS. LINKED IN REFERENCE LIST ###

class vendingmachine:
    def __init__(self, main): #GUI
        self.main = main
        self.main.title("Little Vending Machine") #title of the app on the title bar
        self.main.geometry("400x820") #sets the window size

        #add window icon
        icon = tk.PhotoImage(file="D:/School/Code Lab/Utility App/vendingmachine_icon.png") #link to image
        main.iconphoto(True, icon) #sets the icon to be applied to the whole application (main window and pop-ups, if any)

        ttk.Label( #title at the top of the window
            main, text="Little Vending Machine", font=("Jersey 10", 18, "bold")
        ).pack(pady=3)
        ttk.Label( #message under the title
            main, text='''Hᴇʟʟᴏ! Wʜᴀᴛ ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ʙᴜʏ?''', font=("Jersey 10", 12, "bold")
        ).pack(pady=5)

        self.menu_frame = ttk.Frame(main)
        self.menu_frame.pack(pady=5)

        #call function to display menu
        self.display_menu()

        #create widgets for user inputs
        self.code_label = ttk.Label(main, text="Enter Item Code:")
        self.code_label.pack(pady=5)

        self.code_box = tk.Entry(main) #box for user input
        self.code_box.pack(pady=5)

        self.pay_label = ttk.Label(main, text="Insert Money:")
        self.pay_label.pack(pady=5)

        self.pay_box = tk.Entry(main) #box for user input
        self.pay_box.pack(pady=5)

        self.buy_button = tk.Button(main, text="Purchase", font=("Jersey 10", 12), command=self.purchase)
        self.buy_button.pack(pady=5)

        self.result_label = ttk.Label(main, text="")
        self.result_label.pack()

        self.change_label = ttk.Label(main, text="")
        self.change_label.pack()

    def display_menu(self):
        for category, items in menu.items(): #display items as buttons
            category_label = tk.Label(self.menu_frame, text=category, font=("Jersey 10", 14))
            category_label.pack()

            for code, details in items.items():
                button_text = f"{code}: {details['ID']}"
                
                if details["stock"] == 0: #if item is out of stock, make text color red and don't show price
                    button_text += " - Out of Stock"
                    button_color = "red"
                    button_price = ""
                else:
                    button_price = f" - AED {details['price']:.2f}"
                    button_color = "black"
                    button_text += button_price

                button = tk.Button(self.menu_frame, text=button_text, font=("Jersey 10", 12), fg=button_color,
                                   command=lambda c=code, d=details: self.select_item(c, d))
                button.pack(pady=5)

    def select_item(self, code, details):
        #put code in entry field and selection underneath when item is selected
        self.code_box.delete(0, tk.END)
        self.code_box.insert(0, code)

        self.pay_box.delete(0, tk.END)
        self.result_label.config(text=f"Selected {details['ID']} - AED {details['price']:.2f}")

    def purchase(self):
        item_code = self.code_box.get().upper()
        payment = self.pay_box.get()

        try:
            payment = float(payment)  #convert payment to float
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid amount.")
            return

        item = self.get_item(item_code)
        if item and item["stock"] > 0:
            price = item["price"]
            if payment >= price: #if the payment entered is more than the price, then give change.
                change = payment - price
                item["stock"] -= 1
                self.result_label.config(text=f"Dispensing {item['ID']}...")
                self.change_label.config(text=f"Your change is AED {change:.2f}")
                self.main.after(1500, lambda: self.show_suggestion(item["ID"]))   #show suggestion 1.5 secs after purchase
            else:
                messagebox.showerror("Insufficient payment", f"You need AED {price - payment:.2f} more.")
        elif item :
            messagebox.showerror("Item unavailable", f"Sorry, that item is out of stock. Please select another.")
        else:
            messagebox.showerror("Invalid code", f"Please try again.")

    def get_item(self, code):
        for category, items in menu.items():
            if code in items:
                return items[code]
        return None

    def show_suggestion(self, selected_item=None):
        if not selected_item:
            item_code = self.code_box.get().upper()
            item = self.get_item(item_code)
            if item:
                selected_item = item["ID"]
            else:
                return

        if selected_item and selected_item in suggestions: #shows suggestion
            suggestion = suggestions[selected_item]
            self.result_label.config(text=f"Would you also like {suggestion}? It pairs well with {selected_item}!")
    
#run app
if __name__ == "__main__":
    app = vendingmachine(main)
    main.mainloop()

# -------------------------------
# Utility App - Vending Machine
# Denise Marielle Menguita