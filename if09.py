def main(a):
    x=a%10
    y=a//10
    z=x*10+y
    print(z)
    if z<=a:
        return True
    else:
        return False
print(main(31))