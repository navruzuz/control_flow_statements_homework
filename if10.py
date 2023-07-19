def main(temp):
    if temp<0:
        print("Freezing")
    elif temp>=1 and temp<=10:
        print("Very Cold")
    elif temp>10 and temp<=20:
        print("Cold")
    elif temp>20 and temp<=30:
        print("Normal")
    elif temp>30 and temp<=40:
        print("Hot")
    elif temp>40:
        print("Very Hot")
print(main(23))