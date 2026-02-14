# def add(a,b):
#     sum=a+b
#     return sum
# def sub(a,b):
#     diff=a-b 
#     print(diff)  
# sum=add(2,3)
# print(sum)
# sub(sum,1)







def mul(a,b):
    multi=a*b
    return multi
multiplication=mul(3,2)
def adds(a,b):
    addy=a+b
    print(addy)
    
adds(multiplication,1)



# is_verified=False

def check_Access(is_verified):
    if not is_verified:
        return "access denied"
    else:
        print("nice")
        print("hello")
        print("bye")
        return "acce gran"
    
acc=check_Access(False)
print(acc)




def greeting (name):
    greeting_sen="hello"+name
    return name,greeting_sen
name,sentence=greeting("shubhendu")
print(name)
print(sentence)


def sum_ave(range_value):
    sum=0
    for i in range(range_value):
        sum=sum+i
    avrage=sum/range_value
    return sum,avrage

s,avesum=sum_ave(6)
print(avesum)
print(s)




def show_sal(username):
    ctc=55555
    base=70000
    hra=44444
    pf=55555
    
    return ctc,base,hra,pf
ctc,base,hra,pf=show_sal("shubhendu")
print(ctc)
print(base)
print(hra)
print(pf)