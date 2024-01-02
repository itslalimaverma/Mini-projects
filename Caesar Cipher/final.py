from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
  result = ""
  if direction == "encode":
    for i in range(len(text)):
      if text[i] in alphabet:
        num=alphabet.index(text[i])
        num=num+shift
        if num>=26:
          num=num%26
        result=result+alphabet[num]
      else:
        result+=text[i]
        

        

    print(f"The encrypted text is {result} ")

  elif direction == "decode":
    for i in range(len(text)):
        if text[i] in alphabet:
            num = alphabet.index(text[i])
            num = num - shift
            if num < 0:
                num = num % 26

            result+= alphabet[num]
    print(f"The decrypted text is {result}")
  else:
    print("Please type 'encode' or 'decode'")


continueencrypt=True
while continueencrypt!=False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  result=input("Type 'yes' if you want to continue encrypting. Otherwise type 'no'.\n")
  if result=="no":
    continueencrypt=False
    print("Goodbye!")
  



