def main():
  month = input("Enter a month [ex. March]: ")
  day = int(input("Enter the day [ex. 12]: "))

  if (day > 21 and day < 31 and month == "December") or (day < 20 and day > 0 and month == "January"):
      print("Your zodiac sign is Capricorn")
  elif (day > 19 and day < 31 and month == "January") or (day < 19 and day > 0 and month == "February"):
      print("Your zodiac sign is Aquarius")
  elif (day > 18 and day < 28 and month == "February") or (day < 21 and day > 0 and month == "March"):
      print("Your zodiac sign is Pisces")
  elif (day > 20 and day < 31 and month == "March") or (day < 20 and day > 0 and month == "April"):
      print("Your zodiac sign is Aries")
  elif (day > 19 and day < 30 and month == "April") or (day < 21 and day > 0 and month == "May"):
      print("Your zodiac sign is Taurus")
  elif (day > 20 and day < 31 and month == "May") or (day < 21 and day > 0 and month == "June"):
      print("Your zodiac sign is Gemini")
  elif (day > 20 and day < 30 and month == "June") or (day < 23 and day > 0 and month == "July"):
      print("Your zodiac sign is Cancer")
  elif (day > 22 and day < 31 and month == "July") or (day < 23 and day > 0 and month == "August"):
      print("Your zodiac sign is Leo")
  elif (day > 22 and day < 31 and month == "August") or (day < 23 and day > 0 and month == "September"):
      print("Your zodiac sign is Virgo")
  elif (day > 22 and day < 30 and month == "September") or (day < 23 and day > 0 and month == "October"):
      print("Your zodiac sign is Libra")
  elif (day > 22 and day < 31 and month == "October") or (day < 22 and day > 0 and month == "November"):
      print("Your zodiac sign is Scorpio")
  elif (day > 21 and day < 31 and month == "November") or (day < 22 and day > 0 and month == "December"):
      print("Your zodiac sign is Sagittarius")
  else:
      print("Either a month or a day is invalid!")

  pass

if __name__ == "__main__":
  main()
