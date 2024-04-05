def main():
  wawelenght = int(input("Enter the wavelength in nm: ")) 

  if wawelenght >= 380 and wawelenght < 450 :
      print("The relevant color is Violet")
  elif wawelenght >= 450 and wawelenght < 495 :
      print("The relevant color is Blue")
  elif wawelenght >= 495 and wawelenght < 570 :
      print("The relevant color is Green")
  elif wawelenght >= 570 and wawelenght < 590 :
      print("The relevant color is Yellow")
  elif wawelenght >= 590 and wawelenght < 620 :
      print("The relevant color is Orange")
  elif wawelenght >= 620 and wawelenght <= 750 :
      print("The relevant color is Red")
  else :
      print("Invalid input!")
  pass

if __name__ == "__main__":
  main()
