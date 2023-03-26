def get_fixed_price(discount_rate, discounted_price):
    fixed_price=discounted_price/(1-discount_rate/100)
    return fixed_price
discount_rate=int(input('할인율은?'))
price_a=int(input('A 상품의 할인된 가격은?'))
price_b=int(input('B 상품의 할인된 가격은?'))

original_price_a=get_fixed_price(discount_rate,price_a)
original_price_b=get_fixed_price(discount_rate,price_b)

print('A 상품의 정가는', int(original_price_a),'원')
print('B 상품의 정가는', int(original_price_b),'원')
