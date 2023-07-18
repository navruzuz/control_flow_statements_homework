def main(a):
    if a>0:
        print('a musbat son')
        if a%2==0:
            print('a musbat juft son')
        else:
            print('a musbat toq son')
    if a==0:
        return 0
    else:
        print('a manfiy son')
        if a%2==0:
            print('a manfiy juft son')
        else:
            print('a manfiy toq son')
print(main(-1))