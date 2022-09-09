from shopping_cart import ShoppingCart


class Customer:

    def __init__(self,customerName,customerCart):
        self.name = customerName
        self.shopping_cart = ShoppingCart()

    def addProductToCart(self, productToAdd):
        self.shopping_cart.addProduct(productToAdd)