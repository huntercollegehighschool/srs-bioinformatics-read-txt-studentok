"""
Define a function weightedstring that takes a string input protein. The function returns the weighted string of that protein based on masstable.txt.

weightedstring should read from masstable.txt. It's helpful to have those masses in a dictionary.
"""

def weightedstring(protein):
  table = open('masstable.txt', 'r')
  table_list = table.readlines()
  table_dict = {}
  for i in table_list:
    table_dict[i[:1]] = float(i[2:-2])
  result = 0
  for nucleo in protein:
    result += table_dict.get(nucleo)
  return result

    
  