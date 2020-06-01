'''
@Author: your name
@Date: 2020-06-01 09:00:06
@LastEditTime: 2020-06-01 09:06:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \-Insgram-\test02.py
'''


def log(level, *args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            '''
            * 用来传递任意个无名字参数，这些参数会已一个Tuple的形式来访问；
            ** 用来处理传递任意个有名字的参数，这些参数用dict来访问
            '''
            print(level, 'before calling', func.__name__)
            print(level, 'args:', args, 'kvargs:', kvargs)
            func(*args, **kvargs)
            print(level, 'after calling ', func.__name__)
        return wrapper
    return inner


@log(level='INFO')
def hello(name, msg):
    print('hello', name, msg)


if __name__ == '__main__':
    hello(name='nowcoder', msg='i miss you')
