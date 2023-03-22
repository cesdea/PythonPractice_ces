x=1
while x <6:
    print(x)
    x+=1
else:
    print("1~5반복")
print("\n") 
x=1 
while x<6:
    if x%3:
        print(x)
    else:
        break
    x+=1
else:
    print("1~5반복")
# while-else 의 경우 break로 반복문이 끊길경우 while-else의 else가 작동되지 않는다.
