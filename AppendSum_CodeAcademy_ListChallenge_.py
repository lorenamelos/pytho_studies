def append_sum(lst):
  counter = 0
  while counter < 3:
    lst.append(sum(lst[-2:]))
    counter += 1    
  return lst
print(append_sum([1, 1, 2]))
