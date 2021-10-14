import contextlib
@contextlib.contextmanager
def context_manager(num):
    print('Enter')
    yield num + 1
    print('Exit')
with context_manager(2) as cm:
    print('Right in the middle with cm = {}'.format(cm))
