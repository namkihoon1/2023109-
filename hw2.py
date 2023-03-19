def get_integer(prompt):
    k=int(input(prompt))
    return k

def exchange(money):
    n1=money//500
    money%=500
    n2=money//100
    money%=100
    n3=money//50
    money%=50
    n4=money//10
    print('500원 동전의 개수:',n1)
    print('100원 동전의 개수:',n2)
    print('50원 동전의 개수:',n3)
    print('10원 동전의 개수:',n4)
    
get_integer('동전으로 교환하고자 하는 금액은?')
exchange(3520)
