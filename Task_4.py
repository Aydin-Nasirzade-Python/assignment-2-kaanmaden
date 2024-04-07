def main():
  y=int(input("Enter the year [ex. 2021]: "))
  if y>=0:
      if y%12==8:
          print(f"{y} is the year of the Dragon")
      elif y%12==9:
          print(f"{y} is the year of the Snake")
      elif y%12==10:
          print(f"{y} is the year of the Horse")
      elif y%12==11:
          print(f"{y} is the year of the Sheep")
      elif y%12==0:
          print(f"{y} is the year of the Monkey")
      elif y%12==1:
          print(f"{y} is the year of the Rooster")
      elif y%12==2:
          print(f"{y} is the year of the Dog")
      elif y%12==3:
          print(f"{y} is the year of the Pig")
      elif y%12==4:
          print(f"{y} is the year of the Rat")
      elif y%12==5:
          print(f"{y} is the year of the Ox")
      elif y%12==6:
          print(f"{y} is the year of the Tiger")
      elif y%12==7:
          print(f"{y} is the year of the Hare")
  else:
      print("Invalid year!")
  pass

if __name__ == "__main__":
  main()
