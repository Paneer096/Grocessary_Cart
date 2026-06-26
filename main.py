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

    #3. The SLOT (logic that runs when enter is pressed)
    def process_item():
        #To grab the text cashier typed
        barcode= window.barcode_input.text()

        #To instantly clear the box to put next item
        window.barcode_input.clear()

        #To look up the barrcode in the inventory dictionary
        item = inventory.get_item(barcode)

        if item:
            #if found
            name= item["name"]
            price=item["price"]

            #To add math to running total
            window.running_total += price

            #To push a formatted text string into the List widget(cart_list)
            receipt_line =f"{name}...............................${price:.2f}"
            window.cart_list.addItem(receipt_line)

            #To update the Label (The total price)
            window.total_label.setText(f"Total: ${window.running_total:.2f}")

        else:#if barcode not available or present
            window.cart_list.addItem(f"Error: Barcode {barcode} not found")
        
    #4. To wire the signal and slot
    #when the user presees enter in 'barcode_input', run the 'process_item' function.
    window.barcode_input.returnPressed.connect(process_item)

    #5. To show window and keep the app running
    window.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()