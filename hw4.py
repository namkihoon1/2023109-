def rep_char():
    print(c*n)
def draw_line_string(nstr):
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr*2+4)
    print('f Hello {nstr},')
    print(Welcome to Seoul)
    rep_char('-',nstr*2+4)


msg=input('Input his/her name:')
draw_line_string(nstr)
