def main():
  month = input("Enter name of the month [ex. June]: ")
  day = int(input("Enter the day [ex. 5]: "))

  if (day >= 20 and month == "March") or (day < 21 and month == "June") or (month == "April" or month == "May"):
      print(f"{month} {day} is in Spring")
  elif (day >= 21 and month == "June") or (day < 22 and month == "September") or (month == "July" or month == "August"):
      print(f"{month} {day} is in Summer")
  elif (day >= 22 and month == "September") or (day < 21 and month == "December") or (month == "October" or month == "November"):
      print(f"{month} {day} is in Fall")
  else:
      print(f"{month} {day} is in Winter")
  pass

if __name__ == "__main__":
  main()
