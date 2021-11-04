from random import randint
from string import printable,ascii_letters
from secrets import choice

"""
To implement one time pad into the code, we will need to perform two tasks:
1. generate a random pad 
2. pad the message 

In this course I will perform the above two tasks and the decrypt task, 
The results of each stages will be printed out to the screen.
"""

# below is helper function

# Keep the encrypted code in the Alphabet
def ToAlphabet(number):
    if number > 64:
        return number - 64 if number in range(65,91) else number - 70
    else:
        # handle specific case of blank space " "
        return number - 32
# convert back to get the correct Message
def ConvertBack(number):
    if number > 0:
        return number + 64 if number in range(1,27) else number + 70
    else:
        # handle specific case of blank space " "
        return number + 32


# convert Text to ascii code
def Text_to_ascii(Text : str,inrange = False) -> list:
    """
    :param Text: The string needed to encode to ascii for performing the xor operation
    Text could be message or the key
    :return:
    AsciiArray: a list contain the Ascii codes of all the character from Text
    """

    # Make sure the characters to be printable or valid in python
    for charracter in list(Text):
        if charracter not in printable:
            raise RuntimeError("The text contain unprintable character")
    # get the array of ascii code of characters
    AsciiArray = [ord(character) for character in list(Text)]
    if inrange:
        AsciiArray = [ToAlphabet(num) for num in AsciiArray]
    return AsciiArray



# generate random Pad
def GeneratePad(length : int) ->str:
    """
    :param length: the length of the message to encode
    :return: Pad: the keys to perform encrypting and decrypting message
    """
    PadArr = []
    [PadArr.append(choice(ascii_letters)) for i in range(length)]
    return "".join(PadArr)

# generate text back from ascii list
def AsciiToString(AsciiCode: list,convertback = False) -> str:
    """
    :param AsciiCode: the list contain the ascii code of the text
    :return: Text: the string encode from the ascii code
    """
    if convertback:
        Character = [chr(ConvertBack(code)) for code in AsciiCode]
    else:
        Character = [chr(code) for code in AsciiCode]
    return "".join(Character)

# perfrom Xor operation

def XorOperation(TextCode : list,PadCode : list,convertBack = False) -> list:
    """
    :param TextCode: the list contain ascii codes of the Text
    :param PadCode:  the list contain ascii codes of the Pad
    :return: TargetCode: the list contain ascii codes of the encrypt/decrypt Text
    """
    if len(TextCode) != len(PadCode):
        raise RuntimeError("The text and the key must have the same lenght")
    TargetCode = [TextCode[i] ^ PadCode[i] for i in range(len(PadCode))]
    if convertBack:
        TargetCode = [ConvertBack(code) for code in TargetCode]
    return TargetCode

# the main code

if __name__ == "__main__":
    # get the message to encrypt
    Message = input("Type in your message: ")
    MessageCode = Text_to_ascii(Message,inrange=True)

    # generate the pad key
    PadKey = GeneratePad(len(MessageCode))
    PadCode = Text_to_ascii(PadKey)

    # generate the encrypted message
    EncryptedMessageCode = XorOperation(MessageCode,PadCode)
    EncryptedMessage = AsciiToString(EncryptedMessageCode)

    # decrypt the encrypted message
    DecryptedCode = XorOperation(EncryptedMessageCode,Text_to_ascii(PadKey),convertBack=True)
    DecryptedMessage = AsciiToString(DecryptedCode)

    # print the work
    print("------------------------Encrypt States--------------------------------")
    print(f"Your message Ascii code is      : {MessageCode}")
    print(f"Your Pad Ascii code is          : {PadCode}")
    print(f"Xor product of two array is     : {EncryptedMessageCode}")
    print(f"Which mean the padkey is        : {PadKey}")
    print(f"And the encrypt message is      : {EncryptedMessage}")
    print("------------------------Decrypt States--------------------------------")
    print(f"From the encrypted Message      : {EncryptedMessage}")
    print(f"From the pad                    : {PadKey}")
    print(f"We have the encrypted code      : {EncryptedMessageCode}")
    print(f"and the pad code                : {PadCode}")
    print(f"Which can be used to decrypt as : {DecryptedCode}")
    print(f"The original message is         : {DecryptedMessage}")




