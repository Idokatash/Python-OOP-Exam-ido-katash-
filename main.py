
from order_item import OrderItem
from customer import Customer
from gift import Gift
from regular_order import RegularOrder
from vip_order import VIPOrder


def main():
    item1 = OrderItem(1, "Pizza", 50)
    item2 = OrderItem(2, "Cola", 10)

    regular_customer = Customer(
        101, "ido", "katash",
        "idokatash@gmail.com", "Ramle", "REGULAR"
    )

    vip_customer = Customer(
        102, "David", "Levi",
        "david@gmail.com", "Haifa", "VIP", 20
    )

    regular_order = RegularOrder(
        1001, "Regular Order", "Tel Aviv",
        [item1, item2], regular_customer,
        "CASH", "2026-10-22"
    )

    vip_order = VIPOrder(
        1002, "VIP Order", "Haifa",
        [item1, item2], vip_customer,
        "CREDIT CARD", "2026-10-22"
    )

    print("Regular Order Total:", regular_order.total_price)
    print("VIP Order Total:", vip_order.total_price)

    print("Regular Customer Favorites:")
    for item in regular_customer.favorite_items:
        print(item.item_name)

    gift = Gift()
    vip_customer.take_gift(gift)
    vip_customer.open_gift()


if __name__ == "__main__":
    main()










