def main():
    letter = input("Enter a letter of the alphabet: ")

    if letter == "a" or "e" or "i" or "o" or "u" :
        print("Entered alphabet is a vowel!")
    elif letter == "q" or "w" or "r" or "t" or "y" or "p" or "s" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "z" or "x" or "c" or "v" or "b" or "n" or "m" :
        print("Entered alphabet is a consonant!")
    else :
        print("Sometimes it is a vowel, and sometimes it is a consonant!")
  pass

if __name__ == "__main__":
  main()
