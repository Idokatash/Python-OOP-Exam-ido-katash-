class Order:
    used_ids = set()

    def __init__(self, order_id, name, delivery_address,
                 items, customer, payment_type, order_date):

        if order_id in Order.used_ids:
            raise ValueError("Order ID already exists")

        payments = {"CREDIT CARD", "CASH", "CHECK", "OTHER"}
        if payment_type not in payments:
            raise ValueError("Payment type error")

        item_ids = set()
        for item in items:
            if item.item_id in item_ids:
                raise ValueError("Item ID already exists")
            item_ids.add(item.item_id)

        self.order_id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date

        self.total_price = self.calculate_total_price()

        for item in self.items:
            self.customer.add_favorite_item(item)

        Order.used_ids.add(order_id)

    def calculate_total_price(self):
        total = 0

        for item in self.items:
            total += item.item_price

        return total