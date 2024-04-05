def main():
  month = input("Enter a month [ex. March]: ")
  day = int(input("Enter the day [ex. 12]: "))

  if (day > 21 and month == "December") or (day < 20 and month == "January"):
      print("Your zodiac sign is Capricorn")
  elif (day > 19 and month == "January") or (day < 19 and month == "February"):
      print("Your zodiac sign is Aquarius")
  elif (day > 18 and month == "February") or (day < 21 and month == "March"):
      print("Your zodiac sign is Pisces")
  elif (day > 20 and month == "March") or (day < 20 and month == "April"):
      print("Your zodiac sign is Aries")
  elif (day > 19 and month == "April") or (day < 21 and month == "May"):
      print("Your zodiac sign is Taurus")
  elif (day > 20 and month == "May") or (day < 21 and month == "June"):
      print("Your zodiac sign is Gemini")
  elif (day > 20 and month == "June") or (day < 23 and month == "July"):
      print("Your zodiac sign is Cancer")
  elif (day > 22 and month == "July") or (day < 23 and month == "August"):
      print("Your zodiac sign is Leo")
  elif (day > 22 and month == "August") or (day < 23 and month == "September"):
      print("Your zodiac sign is Virgo")
  elif (day > 22 and month == "September") or (day < 23 and month == "October"):
      print("Your zodiac sign is Libra")
  elif (day > 22 and month == "October") or (day < 22 and month == "November"):
      print("Your zodiac sign is Scorpio")
  elif (day > 21 and month == "November") or (day < 22 and month == "December"):
      print("Your zodiac sign is Sagittarius")
  else:
      print("Invalid input!")

  pass

if __name__ == "__main__":
  main()
