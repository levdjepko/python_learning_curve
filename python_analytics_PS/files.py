# when working with files in python, the best practice is to use the "with" keyword. This way, we don't have to close the file explicitly
with open(file.txt) as file:
  for line in file:
    print(line)
    
