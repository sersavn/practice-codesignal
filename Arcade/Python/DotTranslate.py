#https://codefights.com/arcade/python-arcade/slithering-in-strings/YADembruQtLCmiBKB
#Permutation Chipher

#For password = "iamthebest" and
#key = "zabcdefghijklmnopqrstuvwxy", the output should be
#permutationCipher(password, key) = "hzlsgdadrs".
#
#Here's a table that can be used to encrypt the text:
#
#abcdefghijklmnopqrstuvwxyz
#||  |  ||   |     ||
#vv  v  vv   v     vv
#zabcdefghijklmnopqrstuvwxy

def permutationCipher(password, key):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', key)
    return password.translate(table)
