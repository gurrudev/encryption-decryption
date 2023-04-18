def decrypt(ciphertext, shift):
  decrypted = "" 

  for c in ciphertext:
    if c.isupper():
      c_index = ord(c) - ord('A')

      #shifting to the left
      c_original = (c_index - shift) % 26 + ord('A')

      decrypted += chr(c_original)

    elif c.islower():
      c_index = ord(c) - ord('a')

      #shifting to the left
      c_original = (c_index - shift) % 26 + ord('a')

      decrypted += chr(c_original)

    elif c.isdigit():
      c_original = (int(c) - shift) % 10

      decrypted += str(c_original)

    else:
      decrypted += c

  return decrypted
  
  # check encryption function 

text = 'EXXEGO 8 $ SRI'
s = 4

print('Ciphertext: '+text)
print('Shift: '+str(s)) 
print('Decrypted Text: '+decrypt(text, s))
