
try:
    1/0
except(Exception, BaseException) as e:
    print(e)
else:
    print('No exception')
finally:
    print('Finally')