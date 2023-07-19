def main(a,b,c):
    if a<0 and b<0 and c<0:
        print('3ta manfiy son')
    if (a<0 and b<0) or (c<0 and b<0) or (a<0 and c<0):
        print('2ta manfiy son')
    if (a<0) or (b<0) or (c<0):
        print('1ta manfiy son')
    if (a==0) or (b==0) or (c==0) :
        return 0
print(main(3,-8,0))
    
    # if a<0 and b<0 and c>0:
    #     print('2ta manfiy son')
    # if a<0 and b>0 and c<0:
    #     print('2ta manfiy son')
    # if a>0 and b<0 and c<0:
    #     print('2ta manfiy son')
    # if a>0 and b>0 and c>0:
    #     print(' manfiy son mavjud emas')
    # if a<0 and b<0 and c<0:
    #     print('3ta manfiy son')
    # if a<0 and b<0 and c<0:
    #     print('3ta manfiy son')
    # if a<0 and b<0 and c<0:
    #     print('3ta manfiy son')
    
        