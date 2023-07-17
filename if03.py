def main(a):
    if a>0:
        print(a+1)
        if a==0:
            print(10)
    else:
        print(a-1)
    return  a      
print(main(-5))