def maximo(x,y,z):
  if x > y and x > z:
   return x
  elif y > z and y > x:
   return y
  elif x == y == z:
   return x
  else:
   return z