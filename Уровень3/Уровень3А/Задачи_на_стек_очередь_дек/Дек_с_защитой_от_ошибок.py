#https://algoprog.ru/material/p61

class Deque(object):
  def __init__(self):
    self.array = [None] * 105
    self.count = 0
    self.start = None
    self.tail = None

  def push_front(self, x):
    self.count += 1
    if self.tail is None:
      self.tail = 0
    if self.start is None:
      self.start = 0
    else:
      self.start -= 1
    if self.start == -1:
      self.start = 104
    self.array[self.start] = x
    return 'ok'
  
  def push_back(self, x):
    self.count += 1
    if self.start is None:
      self.start = 0
    if self.tail is None:
      self.tail = 0
    else:
      self.tail += 1
    if self.tail == 105:
      self.tail = 0
    self.array[self.tail] = x
    return 'ok'

  def pop_front(self):
    if self.count == 0:
      return 'error'
    self.count -= 1
    if self.start is None:
      self.start = 0
    el = self.array[self.start]
    self.array[self.start] = None
    self.start += 1
    if self.start == 105:
      self.start = 0
    if self.count == 0:
      self.start = None
      self.tail = None
    return el

  def pop_back(self):
    if self.count == 0:
      return 'error'
    self.count -= 1
    if self.tail is None:
      self.tail = 0
    el = self.array[self.tail]
    self.array[self.tail] = None
    self.tail -= 1
    if self.tail == -1:
      self.tail = 104
    if self.count == 0:
      self.start = None
      self.tail = None
    return el

  def front(self):
    if self.count == 0:
      return 'error'
    return self.array[self.start]

  def back(self):
    if self.count == 0:
      return 'error'
    return self.array[self.tail]

  def size(self):
    return self.count

  def clear(self):
    self.array = [None] * 105
    self.count = 0
    self.start = None
    self.tail = None
    return 'ok'

d = Deque()
while True:
  command = input().split()
  if command[0] == 'push_front':
    print(d.push_front(int(command[1])))
  elif command[0] == 'push_back':
    print(d.push_back(int(command[1])))
  elif command[0] == 'pop_front':
    print(d.pop_front())
  elif command[0] == 'pop_back':
    print(d.pop_back())
  elif command[0] == 'front':
    print(d.front())
  elif command[0] == 'back':
    print(d.back())
  elif command[0] == 'size':
    print(d.size())
  elif command[0] == 'clear':
    print(d.clear())
  else:
    print('bye')
    break
