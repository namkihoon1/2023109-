def read_single_digit(num):
    if num==0:
        return "영"
    elif num==1:
        return "일"
    elif num==2:
        return "이"
    elif num==3:
        return "삼"
    elif num==4:
        return "사"
    elif num==5:
        return "오"
    elif num==6:
        return "육"
    elif num==7:
        return "칠"
    elif num==8:
        return "팔"
    elif num==9:
        return "구"

def read_number(num):
    f=num//100
    s=(num%100)//10
    t=num%10
    
    f_num=read_single_digit(f)
    s_num=read_single_digit(s)
    t_num=read_single_digit(t)
    return f_num+s_num+t_num

real_num=int(input('세 자리 정수 입력:'))
result=read_number(real_num)
print(result)
