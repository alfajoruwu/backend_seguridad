from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt(encrypted_hex):
    # Convert the hex data back to bytes
    encrypted_bytes = bytes.fromhex(encrypted_hex)

    # Load the private key
    with open('private.key', 'rb') as f:
        private_key = RSA.import_key(f.read())

    # Initialize the cipher for decryption
    cipher_rsa = PKCS1_OAEP.new(private_key)

    # Decrypt the data
    decrypted_data = cipher_rsa.decrypt(encrypted_bytes)

    return decrypted_data.decode('utf-8')

# Example encrypted hex data
encrypted_hex = '230cff7913401874a4d3a10b82c53dbafded95593b06bf4808bc6c382fe90723baf3208f29728f7b44d80ca67b200edcbd0b8e4ba742e5b977c6a33f35481d8fc31863bf8f7ad3e6b6d500d0215deb0018f0f9b401968cf4848a6e8b40efcd458525eefbbe41a604eb25e03a8dfd8e325596c66eebece4f3b0d6afa4d38dfca6d7bc714830f0d93d5186751af7202c66f4ed778e457b01defb72e1b73dbaee19725236534dad12615ac893722f5e266bfedd37215f60d356044e83908a5786b501468be96a891983434c40d0395081f1825d5e8341597f8935aac3cb8957b5f785dacbe4a5ca5c5cdd5c945318f7461b4aaef40eea18e9b983ee72e4c62dea0e7bf513ff70e49a9126e1c5c428983facb78f56815da60204e46c70f83bbf74383e0372440af9cef96941cac53ffde0f5b68afb5c3a03792dc69b278036703019121e89f9c75f6cb7993429c3782a15fbd63fff52d25e058fff7a6e450dc479577b4083bed0c50a7ad7a2c7191259825df6ecee4475176c4a44872bdf5a3a3426'

# Decrypt the data
decrypted_log = decrypt(encrypted_hex)
print('Decrypted log:', decrypted_log)