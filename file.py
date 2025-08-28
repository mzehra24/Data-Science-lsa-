try:
  f=open('as.txt')
  print(f.read())
except FileNotFoundError:
  print("file does not exist!")
