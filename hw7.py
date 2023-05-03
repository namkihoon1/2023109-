shopping_bag = {}

while True:
    item = input('상품명? ')
    if item == '':
        break
    quantity = input('수량은? ')
    shopping_bag[item] = int(quantity)
    print(f'장바구니에 {item} {quantity}개가 담겼습니다.')
print(f'\n>>> 장바구니 보기: {shopping_bag}')

search_item = input('\n장바구니에서 확인하고자 하는 상품은? ')
if search_item in shopping_bag:
    print(f'{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다.')
else:
    print(f'{search_item}은(는) 장바구니에 없습니다.')
