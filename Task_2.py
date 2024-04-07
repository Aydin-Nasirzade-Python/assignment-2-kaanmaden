def main():
  month = input("Enter name of the month [ex. June]: ")
  day = int(input("Enter the day [ex. 5]: "))
  if ((month == "April" or month == "May") and 1 <= day <= 31) or ((month == "March") and 20 <= day <= 31) or ((month == "June") and 1 <= day < 21):
      print(f"{month} {day} is in Spring")
  elif ((month == "July" or month == "August") and 1 <= day <= 31) or ((month == "June") and 21 <= day <= 30) or ((month == "September") and 1 <= day < 22):
      print(f"{month} {day} is in Summer")
  elif ((month == "October" or month == "November") and 1 <= day <= 31) or ((month == "September") and 22 <= day <= 30) or ((month == "December") and 1 <= day < 21):
      print(f"{month} {day} is in Fall")
  elif ((month == "January" or month == "February") and 1 <= day <= 31) or (month == "March" and 1 <= day < 20) or (month == "December" and 21 <= day <= 31):
      print(f"{month} {day} is in Winter")
  else:
      print("Invalid")
  pass

if __name__ == "__main__":
  main()
