#https://algoprog.ru/material/p54

class Stack(object):
  def __init__(self):
    self.array = []
    self.length = 0

  def push(self, n):
    self.array.append(n)
    self.length += 1

  def pop(self):
    self.length -= 1
    return self.array.pop()
    
  def back(self):
    return self.array[-1]

  def size(self):
    return self.length

  def clear(self):
    self.array = []
    self.length = 0

if __name__ == "__main__":
  stack = Stack()
  while True:
    command = input().split()
    if command[0] == 'push':
      stack.push(int(command[1]))
      print("ok")
    elif command[0] == 'pop': 
      print(stack.pop())
    elif command[0] == 'back': 
      print(stack.back())
    elif command[0] == 'size': 
      print(stack.size())
    elif command[0] == 'clear':
      stack.clear()
      print("ok")
    else:
      print("bye")
      break
