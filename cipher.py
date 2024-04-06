# User Promted to enter a message and a shift key number which is only accepted as an integer

UserInputMessage = input("Please input a message:")
UserInputMessage = UserInputMessage.lower()
while True:
    try:
        UserInputShiftAmount = int(input("Please input shift key#: "))
        if 1 <= UserInputShiftAmount <= 26:
            break  # If input is within range, exit the loop
        else:
            print("Error: Shift key must be between 1 and 26.")
    except ValueError:
        print("Error: Please enter a valid integer for the shift key.")

# Initialize some variables and import a string function to be able to pull in the alphabet
import string
StandardAlphabet=(string.ascii_lowercase)
ListAlphabet=[]
ShiftedAlphabet=[]
EncryptedMessage=[]

# Run some for loops to autobuild the Caesar Cipher lists
Index=0
for letter in StandardAlphabet:
    ListAlphabet.append(letter)
    if Index >= UserInputShiftAmount:
        ShiftedAlphabet.append(letter)
    Index=Index+1
Index=0
for letter in ShiftedAlphabet:
    if len(ShiftedAlphabet)<len(StandardAlphabet):
        ShiftedAlphabet.append(StandardAlphabet[Index])
        Index=Index+1 
     
# Encrypt the message
for letter in UserInputMessage:
    if letter in StandardAlphabet:
        index = ListAlphabet.index(letter)
        encrypted_letter = ShiftedAlphabet[index]
        EncryptedMessage.append(encrypted_letter)
    else:
        EncryptedMessage.append(letter)

# Print the stuff on screen
print (ListAlphabet)
print(ShiftedAlphabet)
print('Shift Key Requested:', UserInputShiftAmount)
print("Original Message:", UserInputMessage)
print("Encrypted Message:", ''.join(EncryptedMessage))
