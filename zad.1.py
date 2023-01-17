"""Kamil Napieraj lab.03"""

import base64

def szyfrowanie(text):
    text_bytes = text.encode('ascii')
    text_base64_bytes = base64.b64encode(text_bytes)
    text_base64 = text_base64_bytes.decode('ascii')
    return text_base64

def odszyfrowywanie(text_base64):
    text_base64_bytes = text_base64.encode('ascii')
    text_bytes = base64.b64decode(text_base64_bytes)
    text = text_bytes.decode('ascii')
    return text

text = "Kamil Napieraj zad.1"
zaszyfrowany = szyfrowanie(text)
odszyfrowany = odszyfrowywanie(zaszyfrowany)

print("Zaszyfrowany tekst: ", zaszyfrowany)
print("Odszyfrowany tekst: ", odszyfrowany)
