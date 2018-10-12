class Person:
    def __init__(self, name):
        self.name = name


'''
class Person:
    __slots__ = ['name']
    
    def __init__(self, name):
        self.name = name
    
    def __getstate__(self):
        state = (None, {'name' : self.name})
        return state
'''


def demonstrate():
    import pickle
    
    p1 = Person('Guido van Rossum')
    
    with(open('bdfl.pickle', 'wb')) as f:
        pickle.dump(p1, f, protocol=0)
        
    with(open('bdfl.pickle', 'rb')) as f:
        p2 = pickle.load(f)
    
    print(p2.name)


def inspect():
    import my_pickle as pickle
    import pickletools
    p1 = Person('Guido van Rossum')
    pickled = pickle.dumps(p1, protocol=0)
    pickled = pickletools.optimize(pickled)
    print(str(pickled)[2:-2].replace('\\n', '\n'))
    pickletools.dis(pickled)
    p2 = pickle.loads(pickled)
    return p2


def hello_world():
    import pickle
    with(open('hello_world.pickle', 'rb')) as f:
        p = pickle.load(f)


def fizzbuzz():
    import pickle
    with(open('fizzbuzz.pickle', 'rb')) as f:
        p = pickle.load(f)


def make_fizzbuzz():
    import marshal
    import base64
    
    def foo():
        for i in range(1, 16):
            if i % 15 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(str(i))
    
    b64encoded = base64.b64encode(marshal.dumps(foo.__code__))
    
    print("""ctypes
FunctionType
(cmarshal
loads
(cbase64
b64decode
(S{}
tRtRc__builtin__
globals
(tRS''
tR(tR.""".format(str(b64encoded)[1:]))
