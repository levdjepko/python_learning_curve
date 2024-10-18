alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# a function called 'encrypt()' takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    # shift each letter of the 'original_text' forwards in the alphabet
    # by the shift amount and print the encrypted text.
    encrypted_array = []
    for letter in original_text:
        # only encode the letters
        if letter in alphabet:
            # encrypt every single letter by shifting it forward on shift_amount
            encrypted_array += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
    return "".join(encrypted_array)

def decrypt(original_text, shift_amount):
    # shift each letter of the 'original_text' backwards in the alphabet
    # by the shift amount and print the decrypted text.
    decrypted_array = []
    for letter in original_text:
        # only encode the letters
        if letter in alphabet:
            # encrypt every single letter by shifting it forward on shift_amount
            decrypted_array += alphabet[(alphabet.index(letter) - shift_amount) % len(alphabet)]
    return "".join(decrypted_array)

if (direction == "encode"):
    print(encrypt(text, shift))
elif (direction == "decode"):
    print(decrypt(text, shift))



