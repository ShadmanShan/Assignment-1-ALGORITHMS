class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = int(product_id)  # Product id should be an integer
        self.name = name
        self.price = float(price)  # price would be float since decimals are included
        self.category = category

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Category: {self.category}"

    def __lt__(self, other):
        # allows the sorting with prod id
        return self.product_id < other.product_id

def load_products_from_file(filename):
    """Load products from a file, automatically sorting them by product_id."""
    products = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                product = Product(*line.strip().split(','))
                products.append(product)
            except ValueError as e:
                print(f"Error processing line: {line}\n{e}")
    return sorted(products)

def manipulate_products(products):
    """Provide a simple command line interface for manipulating products."""
    operations = {
        '1': insert_product,
        '2': update_product,
        '3': delete_product,
        '4': search_product_by_id,
        '5': search_product_by_name,
        '6': exit_program
    }

    while True:
        choice = input("\n1. Insert\n2. Update\n3. Delete\n4. Search by ID\n5. Search by name\n6. Exit\n Please Choose an operation: ")
        if choice in operations:
            operations[choice](products)
        else:
            print("Invalid choice, please select a valid operation!")

def insert_product(products):
    product_details = input("Enter product details (ID,Name,Price,Category) separated by commas: ").split(',')
    products.append(Product(*product_details))
    print("Product inserted successfully.")

def update_product(products):
    product_id = int(input("Enter product ID to update: "))
    for product in products:
        if product.product_id == product_id:
            name, price, category = input("Enter new name, price, and category separated by commas: ").split(',')
            product.name = name
            product.price = float(price)
            product.category = category
            print("Product updated successfully.")
            return
    print("The Product not found you may need to try again.")

def delete_product(products):
    product_id = int(input("Enter product ID to delete: "))
    products[:] = [product for product in products if product.product_id != product_id]
    print("Product deleted successfully.")

def search_product_by_id(products):
    product_id = int(input("Enter product ID to search: "))
    for product in products:
        if product.product_id == product_id:
            print(product)
            return
    print("The Product not found you may need to try again.")

def search_product_by_name(products):
    product_name = input("Please enter a product name to search: ").lower()
    found_products = [product for product in products if product_name in product.name.lower()]
    if found_products:
        for product in found_products:
            print(product)
    else:
        print("No products found.")

def exit_program(products):
    print("Exiting program...")
    exit()

# Concluding filename and products naming
filename = 'product_datas.txt'
products = load_products_from_file(filename)
manipulate_products(products)
