message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

##y = len(LETTERS)
##x = str(y)
##print"length of text is:" + x

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
    #for symbol in encry:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            #print num
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Hacking key #%s: %s' % (key, translated))
