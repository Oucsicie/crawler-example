import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'begin call'
        func(*args,**kw)
        print 'end call'
    return wrapper


@log
def now():
    print 'something wrong'
