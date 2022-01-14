"""
Define a function weightedstring that takes a string input protein. The function returns the weighted string of that protein based on masstable.txt.

weightedstring should read from masstable.txt. It's helpful to have those masses in a dictionary.
"""

def weightedstring(protein):
  table = open('masstable.txt', 'r')
  table_list = table.read().split()
  counter = 1
  table_dict = {}
  for element in table_list:
    if counter % 2 == 0:
      table_dict.setdefault(element, 0)
    else: 
      prev_element = table_list[counter-2]
      table_dict.setvalue(prev_element, element) 
  print(table_dict)
  