'''
Encrypt an decrypt messages through the function if given a key
'''
########################################

def encrypt(message, key):

    '''the type functions will check the message and key to only be strings or ints'''
    if type(message) == str:
        if type(key) == int:
            '''Converts to a list to able able to modify'''
            listMessage = list(message)
            '''Will only change the values of letters making sure the lower case
            and uppercase letters stay within those boundaries'''
            for i in range (len(listMessage)):
                x = listMessage[i]
                if x.isalpha() == True:
                    newLetter = ord(x) + key
                    if ord(x) > 64 and ord(x) < 91:
                        if newLetter > 90:
                            m = newLetter - 90
                            newLetter = 64 + m
                    if newLetter > 122:
                        m = newLetter - 122
                        newLetter = 96 + m
                    listMessage[i] = chr(newLetter)
                else:
                    continue
            '''Turns the letters in the list back into an encrypted message'''
            finalmessage = "".join(listMessage)
            return finalmessage
        else:
            return 'error'
    else: 
        return 'error'


def decrypt(message, key):

    '''the type functions will check the message and key to only be strings or ints'''
    if type(message) == str:
        if type(key) == int:
            '''Converts to a list to able able to modify'''
            listMessage = list(message)
            for i in range (len(listMessage)):
                x = listMessage[i]
                '''Will only change the values of letters making sure the lower case
                and uppercase letters stay within those boundaries'''
                if x.isalpha() == True:
                    newLetter = ord(x) - key
                    if newLetter < 65:
                        m = 65 - newLetter
                        newLetter = 91 - m
                    if ord(x) < 123 and ord(x) > 96:
                        if newLetter < 97:
                            m = 97 - newLetter
                            newLetter = 123 - m
                    listMessage[i] = chr(newLetter)
                else:
                    continue
            '''Turns the letters in the list back into an encrypted message'''
            finalmessage = "".join(listMessage)
            return finalmessage
        else:
            return 'error'
    else: 
        return 'error'
