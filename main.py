import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

#importing the database
import inventory
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temporary folder and stores its path in sys._MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If running normally via python main.py, look in the current folder
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    #To start the application engine
    app = QApplication(sys.argv)

    #1. To load UI file which we made in Pyside6
    loader = QUiLoader()
    window = loader.load(resource_path("pos_design.ui"))

    #2. To set up a running total variable to keep track of the math
    window.running_total = 0.0
    window.cart_quantities={}

    #3. The SLOT (logic that runs when enter is pressed)
    def process_item():
        #To grab the text cashier typed
        barcode = window.barcode_input.text().strip()

        #To instantly clear the box to put next item
        window.barcode_input.clear()

        if not barcode:
            return

        #To look up the barcode in the inventory dictionary
        item = inventory.get_item(barcode)

        if item:
            name = item["name"]
            price = item["price"]

            #To add math to running total
            window.running_total += price

            #--- NEW QUANTITY TRACKING LOGIC ---
            # If the barcode has been scanned before, increment its count. Otherwise, set it to 1.
            if barcode in window.cart_quantities:
                window.cart_quantities[barcode] += 1
            else:
                window.cart_quantities[barcode] = 1

            # Wipe the visual list box clean so we can rewrite it with updated multipliers
            window.cart_list.clear()

            # Loop through everything currently in the cart and redraw the lines
            for current_barcode, qty in window.cart_quantities.items():
                current_item = inventory.get_item(current_barcode)
                item_name = current_item["name"]
                item_price = current_item["price"]
                
                # If quantity is more than 1, append the (x2), (x3) modifier
                display_name = f"{item_name} (x{qty})" if qty > 1 else item_name
                total_item_cost = item_price * qty

                # Dynamic alignment calculation so dots look even
                dots_count = max(5, 40 - len(display_name) - len(f"${total_item_cost:.2f}"))
                dots = "." * dots_count
                
                receipt_line = f"{display_name}{dots}${total_item_cost:.2f}"
                window.cart_list.addItem(receipt_line)
            #-----------------------------------

            #To update the Label (The total price)
            window.total_label.setText(f"Total: ${window.running_total:.2f}")

        else:#if barcode not available or present
            window.cart_list.addItem(f"Error: Barcode {barcode} not found")
            
        window.cart_list.scrollToBottom()
        
    #4. To wire the signal and slot
    #when the user presees enter in 'barcode_input', run the 'process_item' function.
    window.barcode_input.returnPressed.connect(process_item)

    #5. To show window and keep the app running
    window.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()