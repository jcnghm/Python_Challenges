# Message encryption using rsa package in Python.
# pip install rsa

import rsa

# Set Keys
publicKey, privateKey = rsa.newkeys(512)

# Store message to message variable
message = input("Enter your message: ")

# Encode stored message using public key
encMessage = rsa.encrypt(message.encode(), publicKey)
 
print("Original Message: ", message)
print("Encrypted Message: ", encMessage)

# Decode stored message using private key
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("Decrypted Message: ", decMessage)



#####  OR  #####



# Message encryption using Cryptography package in Python.
# pip install cryptography

from cryptography.fernet import Fernet

# Store message to message variable
message = input("Enter your message: ")

# Set Keys
key = Fernet.generate_key()
fernet = Fernet(key)

# Encoded message
encMessage = fernet.encrypt(message.encode())
 
print("original string: ", message)
print("encrypted string: ", encMessage)

# Decoded Message
decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)