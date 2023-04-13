import nltk
from nltk.corpus import words, names
import ssl
# https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
namelist = names.words()



def encrypt(strng, key):
    temp_string = ""
    for char in strng:
        # print(char)
        # checking for whitespace and added it to string
        if char.isspace():
            shifted_char = ' '
        elif not char.isalpha():
            shifted_char = char
            print(char)
        elif char == char.lower():
            # convert the character to an integer between 0 and 25
            int_num = ord(char.lower()) - ord('a')
            # shift the integer by the key
            shifted_number = (int_num + key) % 26
            # convert the shifted integer back to a character
            shifted_char = chr(shifted_number + ord('a'))
        elif char == char.upper():
            int_num = ord(char.upper()) - ord('A')
            # shift the integer by the key
            shifted_number = (int_num + key) % 26
            # convert the shifted integer back to a character
            shifted_char = chr(shifted_number + ord('A'))
        # add the shifted character to the encrypted string
        temp_string += shifted_char
    return temp_string


def decrypt(strng, key):
    temp_string = ""
    for char in strng:
        # print(char)
        # checking for whitespace and added it to string
        if char.isspace():
            shifted_char = ' '
        elif not char.isalpha():
            shifted_char = char
            print(char)
        elif char == char.lower():
            # convert the character to an integer between 0 and 25
            int_num = ord(char.lower()) - ord('a')
            # shift the integer by the key
            shifted_number = (int_num - key) % 26
            # convert the shifted integer back to a character
            shifted_char = chr(shifted_number + ord('a'))
        elif char == char.upper():
            int_num = ord(char.upper()) - ord('A')
            # shift the integer by the key
            shifted_number = (int_num - key) % 26
            # convert the shifted integer back to a character
            shifted_char = chr(shifted_number + ord('A'))
        # add the shifted character to the encrypted string
        temp_string += shifted_char
    return temp_string


def crack(sentence):
    # Split the sentence into words
    sent_words = sentence.split()
    # Initialize an empty string to hold the decrypted sentence
    decrypted_sentence = ""
    # Iterate over the words in the sentence
    for word in sent_words:
        # Initialize a variable to hold the decrypted word
        decrypted_word = ""
        # Iterate over each possible key value
        for key in range(26):
            # Decrypt the word using the current key
            for char in word:
                if char.isalpha():
                    shifted_num = (ord(char.lower()) - ord('a') - key) % 26
                    decrypted_char = chr(shifted_num + ord('a'))
                else:
                    decrypted_char = char
                decrypted_word += decrypted_char
            # Check if the decrypted word is in the word list
            if decrypted_word.lower() in word_list:
                break  # We found a valid decryption, so stop trying other keys
            else:
                decrypted_word = ""  # Reset the decrypted word if it wasn't found in the word list
        # Add the decrypted word to the decrypted sentence
        decrypted_sentence += decrypted_word + " "
    # Remove the trailing space from the decrypted sentence and return it
    return decrypted_sentence[:-1]


    # compare each word to the nltk word list
    # come up with % of numbers that make sense
# crack('The cat went to the bar')


