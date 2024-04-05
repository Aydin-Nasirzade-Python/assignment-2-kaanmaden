
def main():
  year = int(input("Enter the year [ex. 2021]: "))

  if (year - 2000) % 12 == 0 :
      print("2010 is the year of the Dragon")
  elif (year - 2000) % 12 == 1 :
      print("2010 is the year of the Snake")
  elif (year - 2000) % 12 == 2 :
      print("2010 is the year of the Horse")
  elif (year - 2000) % 12 == 3 :
      print("2010 is the year of the Sheep")
  elif (year - 2000) % 12 == 4 :
      print("2010 is the year of the Monkey")
  elif (year - 2000) % 12 == 5 :
      print("2010 is the year of the Rooster")
  elif (year - 2000) % 12 == 6 :
      print("2010 is the year of the Dog")
  elif (year - 2000) % 12 == 7 :
      print("2010 is the year of the Pig")
  elif (year - 2000) % 12 == 8 :
      print("2010 is the year of the Rat")
  elif (year - 2000) % 12 == 9 :
      print("2010 is the year of the Ox")
  elif (year - 2000) % 12 == 10 :
      print("2010 is the year of the Tiger")
  elif (year - 2000) % 12 == 11 :
      print("2010 is the year of the Hare")
  else :
      print("Invalid year!")
  pass

if __name__ == "__main__":
  main()
