class ShoppingCart:

    def __init__(self):
        self.all_products = []
    
    def addProduct(self, productToAdd):
        self.all_products.append(productToAdd)
        print(f"Added {productToAdd.name} to the cart.")
    
    def getProductTotal(self):
        totalPrice = 0
        for self in self.all_products:
            totalPrice += self.price
        print (f"Your total cart value is ${totalPrice}.")

        
    def removeAllProducts(self):
        del self.all_products[:]
        print ("All items removed from cart.")