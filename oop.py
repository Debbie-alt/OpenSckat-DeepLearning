class Dog():
    def __init__(self, breed, size):
        self.breed = breed
        self.size = size
        print("THe dog's name is {}".format(self.name))
    def eat(self, food):
        print("The {} bread loves eba {}".format(self.breed, food))
    def sleep_time(self, time):
        print("The {} dog loves to sleep at 6".format(self.breed))        