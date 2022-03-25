#Disclaimer
#This code is not original and is implemented as a practice tutorial to improve oneself understanding towards 
#python dunder methods.
#The tutorial and explanation could be found on
#https://medium.com/mlearning-ai/dancing-with-python-dunder-methods-b5d89172b622


class Quaternion:
  def __init__(self, a, b, c, d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d

  def __repr__(self):
    return (f'Quaternion(a={self.a}, b={self.b}, c={self.c}, d={self.d})')
  
  def __sub__(self, other):
    return Quaternion(self.a-other.a,
                      self.b-other.b,
                      self.c-other.c,
                      self.d-other.d)
    
  def __add__(self, other):
    return Quaternion(self.a+other.a,
                      self.b+other.b,
                      self.c+other.c,
                      self.d+other.d)
  
  def __mul__(self, other):
    return Quaternion(self.a * other.a -
                      self.b * other.b -
                      self.c * other.c -
                      self.d * other.d,
                      
                      self.a * other.b +
                      self.b * other.a +
                      self.c * other.d -
                      self.d * other.c,
                      
                      self.a * other.c +
                      self.c * other.a +
                      self.d * other.b -
                      self.b * other.d,
                      
                      self.a * other.d +
                      self.d * other.a +
                      self.b * other.c -
                      self.c * other.b)
  
  def __neg__(self):
    return Quaternion(-self.a,
                      -self.b,
                      -self.c,
                      -self.d)
    

Q1 = Quaternion(1, 0, 1, 2)
Q2 = Quaternion(-1, 1, 2, .5)
Q3 = Quaternion(-0.5, 0, -1, -2.5)


class BoolArray:
  def __init__(self, condition):
    self.condition = condition
  
  def __and__(self, other):
    assert len(self.condition) == len(other)
    return BoolArray([b1 and b2 for (b1, b2) in zip(self.condition, other)])

  def __or__(self, other):
    assert len(self.condition) == len(other)
    return BoolArray([b1 or b2 for (b1, b2) in zip(self.condition, other)])

  def __invert__(self):
    return BoolArray([not(b) for b in self.condition])
  
  def __call__(self):
    return self.condition

  def __len__(self):
    return len(self.condition)
  
  def __iter__(self):
    for el in self.condition:
      yield el


b = BoolArray([True, False, True, False])
b1 = BoolArray([True, False, True, False])
b2 = BoolArray([False, False, True, True])
b3 = BoolArray([True, True, True, True])


((b1 | b2) & b3)()