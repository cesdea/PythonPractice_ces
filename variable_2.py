global outer
outer='out'
def ban():
    inner='in'
    global check
    check='true'
    inner='lier'
    print("inner:",inner)
    # print("outer:",outer) 찾을 수 없는 변수
    outer=inner
    print("outer:",outer)
    print("check:",check)
ban()
# print("inner:",inner) 찾을수 없는 변수
print("outer:",outer)
print("check:",check)