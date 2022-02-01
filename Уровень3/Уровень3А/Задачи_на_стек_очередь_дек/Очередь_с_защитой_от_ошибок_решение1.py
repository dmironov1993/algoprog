from collections import deque

if __name__ == "__main__":
  d = deque()
  length = 0
  while True:
    command = input().split()
    if command[0] == 'push':
      d.append(int(command[1]))
      length += 1
      print('ok')
    elif command[0] == 'pop':
      if length > 0:
        length -= 1
        print(d.popleft())
      else:
        print('error')
    elif command[0] == 'front':
      if length > 0:
        print(d[0])
      else:
        print('error')
    elif command[0] == 'size':
      print(length)
    elif command[0] == 'clear':
      d = deque()
      length = 0
      print('ok')
    else:
      print('bye')
      break
