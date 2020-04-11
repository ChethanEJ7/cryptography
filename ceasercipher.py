def encrypt(text,s):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
      # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

#check the above function

#text = "CEASER CIPHER DEMO"
print "Enter the text to encrypt using Ceaser Cipher: "
t = raw_input()
text = str(t)


y = len(t)
x = str(y)
print"length of text is:" + x

print "Enter the Shift key: "
skey = raw_input()
s=int(skey)


print "Plain Text : " + text
print "Shift Position : " + str(s)
print "Cipher Text: " + encrypt(text,s)
