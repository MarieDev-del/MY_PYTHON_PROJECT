#Encryption:is a plain text converted to cipher text En(x)=(X+n)mod26 
#Decryption:is a cipher text converted into plain  Dn(x)=(X-n)mod26
#cipher text use shift key
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encryption(plain_text,shift_key):
    cipher_text = ''
    for char in plain_text:
        position = letters.index(char)
        new_position = (position + shift_key)%26
        cipher_text+=letters[new_position]
    print(cipher_text)
def decryption(cipher_text,shift_key):
    plain_text =''
    for char in cipher_text:
        position = letters.index(char)
        new_position= (position-shift_key)%26
        plain_text+=letters[new_position]
    print(plain_text)


Want_to_end = False
while not Want_to_end:   
    text = input("Type a text: ").upper()
    shift = int(input("Type your preffered shift_key: "))
    What_to_do = input("Type what you want to do,Encrypt or Decrypt: ")
    if What_to_do == 'Encrypt' or What_to_do == 'encrypt':
        encryption(plain_text=text,shift_key=shift)
    elif What_to_do == 'Decrypt' or What_to_do == 'decrypt':
        decryption(cipher_text=text,shift_key = shift)
    play_again =input('Do you want to end or continue.Type yes/no: ')    
    if play_again=='no' or play_again=='No':
        Want_to_end = True
        print('Bye')
    
        
        
        
        