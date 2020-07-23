
"""
There are two lists of different lengths. The first contains keys, and the second contains values.
Write a function that creates a dictionary from these keys and values.
If the key did not have enough value, the dictionary should have the value None.
Values that did not have enough keys should be ignored.
"""

def createDict(list1, list2):
  mydict = {}
  for i in range(len(list1)):
    if i < len(list2):
      mydict[list1[i]] = list2[i]
    else: mydict[list1[i]] = None
  return mydict


list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

print("List 1 -> {}".format(list1))
print("List 2 -> {}".format(list2))
mydict = createDict(list1, list2)
print(mydict)
