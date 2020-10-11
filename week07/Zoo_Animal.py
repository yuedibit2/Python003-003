from abc import ABCMeta,abstractmethod
class Zoo(object):
    animals={}
    def __init__(self,name):
        self.name=name
    @classmethod
    def add_animal(cls,animal):
        if animal not in cls.animals:
            cls.animals[animal]=animal
        else :
            pass
        if not hasattr(cls,animal.__class__.__name__):
            setattr(cls,animal.__class__.__name__,animal)

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,name,category,body_type,character):
        self.name=name
        self.category=category
        self.body_type=body_type
        self.character=character
    @property
    def is_ferocious(self):
        body_dict={'小':1,'中等':2,'大':3}
        return (body_dict[self.body_type]>=2 and self.category=='食肉' and self.character=='凶猛')
    @property
    def is_pet(self):
        return not self.is_ferocious


class Cat(Animal):
    call='meow'
    def __init__(self,name,category,body_type,character):
        super().__init__(name,category,body_type,character)

class Dog(Animal):
    call='woof'
    def __init__(self,name,category,body_type,character):
        super().__init__(name,category,body_type,character)

if __name__=='__main__':
    z=Zoo('时间动物园')
    cat1=Cat('大花猫1','食肉','小','温顺')
    z.add_animal(cat1)
    have_cat=hasattr(z,'Cat')