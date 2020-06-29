class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print('Object created: ', s)
s1 = Singleton()
print('Object created; ', s1)


# Отложенный экземпляр в Singleton

class Singleton_1(object):

    __instance = None

    def __init__(self):
        if not Singleton_1.__instance:
            print('__init_- method called..')
        else:
            print('Instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton_1()
        return cls.__instance


a = Singleton_1() # class initialized, but object not created
print('Object created: ', a.getInstance()) # Object created
a1 = Singleton_1() #instance already created