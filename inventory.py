#This is invetory
#Dictionary datatype is used to create this database (Nested Dictionary)

items_database = {
    "1001": {"name":"Bread", "price": 20},
    "1002": {"name":"milk",  "price": 30},
    "1003": {"name":"banana", "price":60}    
    }

def get_item(barcode):
    #To get access the item
    return items_database.get(barcode)