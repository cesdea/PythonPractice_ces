def f(a, b):
    try:
        if a and b:                  # a와 b가 둘 다 0이 아닐 때
          return (a * b) + (a / b)
        elif a:                      # 그렇지 않고 a만 0이 아닐 때
          return '불능'
        else:                        # 둘 다 0일 때
          return '부정' 
    except:
        return "오류내지마라"

print(f('ㅇ', 500000))