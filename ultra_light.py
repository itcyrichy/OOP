class Animal:
    def __init__(self,kind,weight,age,food):
        self.kind = kind
        self.weight = weight
        self.age = age
        self.__food = food
    def __str__(self):
        return f'Вид: {self.kind}, вес: {self.weight}, возраст: {self.age}'
    def count_some_index(self):
        return self.weight*self.age/2*100


Bob = Animal('cat',80,20,'meat')
print(Bob.count_some_index())
print(Bob)
# print(Bob.__food)

class Bird(Animal):
    def __init__(self,kind,weight,age,food,size):
        super().__init__(kind,weight,age,food)
        self.size=size
    def count_some_index(self):
        return self.weight * self.size

Lilo = Bird('owl',2,0.5,'mice',3)
print(Lilo)
print(Lilo.count_some_index())