class Customer:
    used_ids = set()

    def __init__(self, customer_id, first_name, last_name,
                 email, delivery_address, customer_type,
                 customer_discount=None):

        if customer_id in Customer.used_ids:
            raise ValueError("Customer ID already exists")

        customers = {"REGULAR", "VIP"}
        if customer_type not in customers:
            raise ValueError("Customer type has to be REGULAR or VIP")

        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = []
        self.customer_gift = None

        Customer.used_ids.add(customer_id)

    def add_favorite_item(self, item):
        for favorite in self.favorite_items:
            if favorite.item_name == item.item_name:
                return

        self.favorite_items.append(item)

    def remove_favorite_item(self, item):
        for favorite in self.favorite_items:
            if favorite.item_name == item.item_name:
                self.favorite_items.remove(favorite)
                return

    def take_gift(self, gift):
        self.customer_gift = gift

    def open_gift(self):
        if self.customer_gift is not None:
            self.customer_gift.open_gift()