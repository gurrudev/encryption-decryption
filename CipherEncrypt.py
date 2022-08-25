def encrypt(plaintext, shift):
  encrypted = ""

  for c in plaintext:
    if c.isupper():
      #subtracting the unicode of 'A' 65 to get the index in [0-25] range
      c_index = ord(c) - ord('A')

      #shift the charecter
      c_shift = (c_index + shift) % 26 + ord('A')

      encrypted += chr(c_shift)
    
    elif c.islower():
      #subtracting the unicode of 'a' 97 to get the index in [0-25] range
      c_index = ord(c) - ord('a')

      #shift the charecter
      c_shift = (c_index + shift) % 26 + ord('a')

      encrypted += chr(c_shift)
    
    elif c.isdigit():
      c_shift = (int(c) + shift) % 10

      encrypted += str(c_shift)

    else:
      #if nither a character nor a number - leave as it is

      encrypted += c

  return encrypted
    
  
text = 'ATTACK 4 $ ONE'
s = 4

print('Plaintext: '+text)
print('Shift: '+str(s))
print('Encrypted Text: '+encrypt(text, s))
