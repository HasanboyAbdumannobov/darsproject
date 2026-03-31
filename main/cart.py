from decimal import Decimal


class Cart:
    SESSION_KEY = 'cart'

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(self.SESSION_KEY, {})

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = 0
        self.cart[product_id] += quantity
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrease(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] -= quantity
            if self.cart[product_id] <= 0:
                del self.cart[product_id]
            self.save()

    def clear(self):
        self.session[self.SESSION_KEY] = {}
        self.save()

    def save(self):
        self.session[self.SESSION_KEY] = self.cart
        self.session.modified = True

    def __len__(self):
        return sum(self.cart.values())

    def total_price(self, products_map):
        total = Decimal('0.00')
        for product_id, quantity in self.cart.items():
            product = products_map.get(int(product_id))
            if product:
                total += product.price * quantity
        return total