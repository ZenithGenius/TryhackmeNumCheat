#!/bin/env python
import os
import sys
length = len(sys.argv)
if length != 3:
  print("\n\nUsage: python main.py <file_name> <number_of_characters>")
else:
  file_name = sys.argv[1]
  try: int(sys.argv[2])
  except ValueError or TypeError:
    print('\n\nEnter a valid number for the number of characters needed.')
    exit()
  num_of_char = int(sys.argv[2])
  if os.path.exists(file_name):
    with open(file_name, 'r') as file:
      for line in file:
        line0 = line.strip('\n')
        if len(line0) == num_of_char:
          with open('output.txt','a') as f:
            f.write(line)
          word = f'{line0}',str(len(line0))
          print('\n',word)
  else:
    print('Enter a valid path, file does not exist.')
    exit()
  print(f'''
\n\n Le nouveau fichier "output.txt" a ete cree et est a \n\n {os.path.abspath("output.txt")}
Supprimer output.txt avant de relancer le code en ecrivant :  \n\n\t\t
sudo rm -f {os.path.abspath("output.txt")} ou \n\n echo '' > {os.path.abspath("output.txt")}
''')
