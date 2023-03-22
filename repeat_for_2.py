for x in range(1,5):
    print(x)
else:
    print("리스트의 원소를 모두 출력했어요")
print("\n")    
for x in range(1,5):
    if x%3:
        print(x)
    else:
        break
else:
    print("리스트의 원소를 모두 출력했어요")
# for-else 의 경우 break로 반복문이 끊길경우 for-else의 else가 작동되지 않는다.