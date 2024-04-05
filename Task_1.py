def main():
    letter = input("Enter a letter of the alphabet: ")

    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("Entered alphabet is a vowel!")
    elif letter == "q" or letter == "w" or letter == "r" or letter == "t" or letter == "p" or letter == "s" or letter == "d" or letter == "f" or letter == "g" or letter == "h" or letter == "j" or letter == "k" or letter == "l" or letter == "z" or letter == "x" or letter == "c" or letter == "v" or letter == "b" or letter == "n" or letter == "m":
        print("Entered alphabet is a consonant!")
    else:
        print("Sometimes it is a vowel, and sometimes it is a consonant!")

  pass

if __name__ == "__main__":
  main()
