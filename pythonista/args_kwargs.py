def names(*args):
    for name in args:
        print(name)


names('Harshith','kumar','NG')

def names2(**kwargs):
    for key,value in kwargs.items():
        print('{}:{}'.format(key,value))

names2(First='Harshith', Middle ='Kumar',Last ='NG')

def name3(*phone, **name):
    for key,value in name.items():
        print('{}:{}'.format(key,value))
    for num in phone:
        print('Contact:',num)
name3(8105588465,8073897233,First='Harshith', Middle ='Kumar',Last ='NG')
