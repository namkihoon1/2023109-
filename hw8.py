def shopping_cart():
    cart = {}
    while True:
        item = input("상품명?")
        if item == "":
            break
        quantity = int(input("수량은? "))
        cart[item] = quantity
        print(f"장바구니에 {item} {quantity}개가 담겼습니다.")
    
    print(f"\n>>> 장바구니 보기: {cart}")
    
    search_item = input("\n장바구니에서 확인하고자 하는 상품은? ")
    if search_item in cart:
        print(f"{search_item}(은)는 {cart[search_item]}개 담겨 있습니다.")
    else:
        print(f"{search_item}(은)는 장바구니에 없습니다.")

shopping_cart()
