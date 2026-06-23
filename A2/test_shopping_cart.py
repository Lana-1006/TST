from shopping_cart import ShoppingCart

def test_empty_cart_has_zero_total():
    cart = ShoppingCart()
    assert cart.get_total() == 0
