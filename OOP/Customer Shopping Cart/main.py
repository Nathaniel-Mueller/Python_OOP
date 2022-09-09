from shopping_cart import ShoppingCart
from product import Product
from customer import Customer



# Defined products

product1 = Product("milk", 3.50, "Dairy")
product2 = Product ("chocolate", 5, "Candy")
product3 = Product("ham", 12, "Meat")

# Defined shopping carts

cart1 = ShoppingCart

# Defined customers

customer1 = Customer("Lily", cart1)

print ("")

print(f"The customer's name is {customer1.name}.")

print ("")

customer1.addProductToCart(product1)
customer1.addProductToCart(product2)
customer1.addProductToCart(product3)

print ("")

for products in customer1.shopping_cart.all_products:
    print (products.name)

print ("")

customer1.shopping_cart.getProductTotal()

print ("")

customer1.shopping_cart.removeAllProducts()

print ("")

print (customer1.shopping_cart.all_products)