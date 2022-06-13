#functional
#sort an array of integers in ascending order

def sort(array):
  arr = []
  for item in array:
      arr.append(item)
  return sorted(arr)

list1 = [4, 3, 8, 80, 30, 2, 60]
print(sort(list1))


#Object oriented
#Podracers

class Podracers:
  def __init__(self, name, max_speed, condition, price):
    self.name = name
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"
    print(self.condition)

class AnakinsPod(Podracers):
  def __init__(self, name, max_speed, condition, price):
    super().__init__(name, max_speed, condition, price)
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def boost(self):
    self.max_speed *= 2
    print(self.max_speed)

class SebulbasPod(Podracers):
  def __init__(self, name, max_speed, condition, price):
    super().__init__(name, max_speed, condition, price)
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def flame_jet(self, podracer):
    podracer.condition = 'trashed'
    print(podracer.name, 'was trashed')

my_pod = AnakinsPod('racer', 100, 'repaired', 20000)
trevons_pod = SebulbasPod('crusher', 90, 'perfect', 19000)

trevons_pod.flame_jet(my_pod)
my_pod.repair()
my_pod.boost()

# encapsulation is practiced in our classes methods. They save time compared to a functional approach
#this uses inheritance because AnakinsPod, and SebulbasPod classes inherit the Podracers class. 

# I believe OOP was the right coding style for this problem, because it saves time and is easy to understand