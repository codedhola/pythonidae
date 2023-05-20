from cryptography import encode, decode

cipher_type = input("Type 'encode' to encrypt, 'decode' to decrypt: \n")
message_value = input("Type your message: \n")
shift_value = int(input("Input a Shift Value: "))

cipher_message =""
if cipher_type == "encode":
    cipher_message += encode(message_value, shift_value)
else: 
    cipher_message += decode(message_value, shift_value)

print(f"Your cipher message is => {cipher_message}")
# print(encode("dez"))
# print(decode("hid"))