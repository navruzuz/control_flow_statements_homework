def main(a,b,c):
    if a>0 and b>0 and c>0:
        print('3ta')
    if a<0 and b>0 and c>0:
        print('2ta')
    if a>0 and b<0 and c>0:
        print('2ta')
    if a>0 and b>0 and c<0:
        print('1ta')
    if a<0 and b<0 and c>0:
        print('1ta')
    if a>0 and b<0 and c<0:
        print('1ta')
    if a<0 and b>0 and c<0:
        print('1ta')
    if a==0 and b==0 and c==0:
        print('0ta')
print(main(2,5,6))