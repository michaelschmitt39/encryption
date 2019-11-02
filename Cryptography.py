# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:46:40 2019

@author: xfang13
"""

#The plain text 
plain_text = "Talks between the United Auto Workers union and General Motors \"have taken a turn for the worse, according to the union's chief negotiator, suggesting that no immediate end is in sight for the auto industry's longest strike in decades. The setback in talks followed several days of reported progress between the two sides. They hope to reach a new four-year deal. Terry Dittes, the vice president of the United Auto Workers union negotiating team, sent a letter to members midday Sunday saying that the union found the company's latest contract proposal to be totally unacceptable to the union."

def look_up_list_gen(text):
    return list(text)  # I  delete the function 'set'


class CaesarCipher:
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    def __init__(self, key):
        assert(key > 0 and type(key) == int)
        self.key = key
        
                
    def encrypt(self, plain_text):
        # self.plain_text = plain_text
        cipher_text = look_up_list_gen(plain_text)
        encrypt_text = ''
        for letter in cipher_text:
            letter = letter.lower()
            if letter in self.alphabet:
                encrypt_text += self.alphabet[(self.alphabet.index(letter) + self.key) % 26 ]
            else:
                encrypt_text += letter
        self.cipher_text = encrypt_text


        
        
    def decrypt(self, plain_text):
        cipher_text = look_up_list_gen(plain_text)
        decrypt_text = ''

        for letter in cipher_text:
            if letter in self.alphabet:
                decrypt_text += self.alphabet[(self.alphabet.index(letter) - self.key) % 26 ]
            else:
                decrypt_text += letter

        return decrypt_text
        
        
        

class VigenereCipher:
    def __init__(self, key, look_up_list):
        assert(type(key) == str)
        self.key = key
        
    def encrypt(self, plain_text):
        assert(len(self.key) <= len(plain_text))
        
    def decrypt(self):
        pass
                   
            
if __name__ == "__main__":
    caesar = CaesarCipher(3)
    caesar.encrypt(look_up_list_gen(plain_text))
    print("Encrypted text: ",caesar.cipher_text)
    print("""
                ---------------------------- 
    """)
    print("Decrypted text: ",caesar.decrypt(caesar.cipher_text).capitalize())

    #vigenere = VigenereCipher(plain_text[:5],look_up_list_gen(plain_text))
    #vigenere.encrypt(plain_text)
    #print("Encrypted text: ",vigenere.cipher_text)
    #print("Decrypted text: ",vigenere.decrypt())                         
