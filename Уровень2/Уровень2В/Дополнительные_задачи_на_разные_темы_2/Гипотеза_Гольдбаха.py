def primes(n):
  prime = [True] * (n + 1)
  prime[0] = prime[1] = False
  for i in range(2, int(n**0.5) + 1):
    if prime[i]:
      for j in range(i*i, n + 1, i):
        prime[j] = False
  return prime

if __name__ == "__main__":
  n = int(input())
  prime_list = primes(n)
  for i in range(2, n + 1):
    if prime_list[i] and prime_list[n - i]:
      print(i, n - i)
      break
