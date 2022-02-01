class Queue(object):
  def __init__(self):
    self.stack1 = []
    self.length1 = 0
    self.stack2 = []
    self.length2 = 0

  def push(self, n):
    if self.length1 == 0:
      self.stack1.append(n)
      for i in range(self.length2):
        self.stack1.append(self.stack2[i])
      self.stack2 = []
      self.length1 = self.length2 + 1
      self.length2 = 0
    else:
      self.stack2.append(n)
      for i in range(self.length1):
        self.stack2.append(self.stack1[i])
      self.stack1 = []
      self.length2 = self.length1 + 1
      self.length1 = 0
    return 'ok'

  def pop(self):
    if self.length1 > 0:
      self.length1 -= 1
      return self.stack1.pop()
    elif self.length2 > 0:
      self.length2 -= 1
      return self.stack2.pop()
    else:
      return 'error'

  def front(self):
    if self.length1 > 0:
      return self.stack1[self.length1 - 1]
    elif self.length2 > 0:
      return self.stack2[self.length2 - 1]
    else:
      return 'error'

  def size(self):
    return self.length1 + self.length2

  def clear(self):
    self.stack1 = []
    self.length1 = 0
    self.stack2 = []
    self.length2 = 0
    return 'ok'

if __name__ == "__main__":
  q = Queue()
  while True:
    command = input().split()
    if command[0] == 'push':
      print(q.push(int(command[1])))
    elif command[0] == 'pop':
      print(q.pop())
    elif command[0] == 'front':
      print(q.front())
    elif command[0] == 'size':
      print(q.size())
    elif command[0] == 'clear':
      print(q.clear())
    else:
      print('bye')
      break
