def main():
  x=float(input("Enter x: "))
  y=float(input("Enter y: "))
  if x**2 +y**2 <=1 and y>=0 and x>=0 and y>=x or\
     x**2 +y**2 <=1 and y>=0 and y>=-x and x<=0 or\
     x**2 +y**2 <=1 and x>=0 and y<=0 and y>=-x or\
     x**2 +y**2 <=1 and x<=0 and y<=0 and y>=x or\
     x**2 +y**2 >=1 and y<=0 and x>=0 and y<=-x or\
     x**2 +y**2 >=1 and y<=0 and x<=0 and y<=x:
      print("The point is in the shaded area")
  else:
      print("The point is not in the shaded area")
  pass

if __name__ == "__main__":
  main()
