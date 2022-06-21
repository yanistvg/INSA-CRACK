import random
import string

msg = "<censored>"

def change_lettre(letter1 : str, letter2 : str, i : int) -> str:
	letter1 = chr(ord(letter1) % i)
	letter1 = chr(ord(letter1) ^ ord(letter2))
	return letter1


def autoHash(msg : str) -> str:
	res = []
	key = random.choice(string.ascii_letters)
	y = 1
	for i in range(len(msg)):
		res.append(change_lettre(msg[i], key, y))
		y += 1
		key = msg[i]
	res.append(key)
	return ''.join(res)

# f = open("out.txt", "w+")
# f.write(autoHash(msg))
# f.close()