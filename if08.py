def main(a):
    if a%2==0:
        print('a juft son')
        if (a%10)%2==0 and a>10 and a<100 :
            print('a ikki xonali juft son')
        if (a%10)%2!=0 and a>10 and a<100 :
            print('a ikki xonali toq son')
        if (a%100)%2==0 and a>100 and a<1000:
            print('a uch xonali juft son')
        if (a%100)%2!=0 and a>100 and a<1000:
            print('a uch xonali toq son')
    else:
        print('a toq son')
        if (a%10)%2==0 and a>10 and a<100 :
            print('a ikki xonali juft son')
        if (a%10)%2!=0 and a>10 and a<100 :
            print('a ikki xonali toq son')
        if (a%100)%2==0 and a>100 and a<1000:
            print('a uch xonali juft son')
        if (a%100)%2!=0 and a>100 and a<1000:
            print('a uch xonali toq son')
        
        # if (a%10)%2==0 :
        #     print('a ikki xonali juft son')
        # if (a%100)%2==0:
        #     print('a uch xonali juft son')
        # if (a%10)%2!=0 :
        #     print('a ikki xonali toq son')
        # if (a%100)%2!=0 :
        #     print('a uch xonali toq son')
print(main(321))
    
