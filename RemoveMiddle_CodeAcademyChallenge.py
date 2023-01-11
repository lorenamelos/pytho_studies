'''Our next function will remove all elements from a list with an index within a certain range. 
The function will accept a list, a starting index, and an ending index. 
All elements with an index between the starting and ending index should be removed from the list.'''

def remove_middle (lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
