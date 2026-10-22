
from order import Order


class VIPOrder(Order):
    def calculate_total_price(self):
        if self.customer.customer_type != "VIP":
            raise ValueError("Customer must be VIP")

        total = super().calculate_total_price()

        discount = self.customer.customer_discount

        if discount is None:
            discount = 0

        return total * (1 - discount / 100)
