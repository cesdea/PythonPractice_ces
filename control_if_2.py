s='banana'
if 'a' in s:
    if 'b' in 'banana':
        print('banana에는 a도 있고 b도 있어요!')

if 'a' in s and 'b' in 'banana':
    print('banana에는 a도 있고 b도 있어요!')

if 'a' in s or 'c' in 'banana':
    print('banana에는 a 또는 c도 있어요!')
