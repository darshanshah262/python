def fact(n):
  res = 1
  for i in range(2, n + 1):
    res = res * i
  return res

def count_heads(n, r):
  output = fact(n) / (fact(r) * fact(n - r))
  output = output / (pow(2, n))
  return output

n,r = list(map(int,(input().split())))
print(count_heads(n,r))