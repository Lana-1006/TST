from shopping_cart import ShoppingCart

def test_empty_cart_has_zero_total():
    cart = ShoppingCart()
    assert cart.get_total() == 0
    
def test_add_item_increases_total():
    cart = ShoppingCart()
    cart.add_item(10)
    assert cart.get_total() == 10

def test_add_multiple_items_sums_total():
    cart = ShoppingCart()
    cart.add_item(10)
    cart.add_item(5)
    assert cart.get_total() == 15
    
