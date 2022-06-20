chaine = "Chere moi,\nj'ai bien travailler"

def get_chaine_from_file(file : str) -> str:
	f = open(file, "r")
	tmp = f.read()
	f.close()
	return tmp

def get_key(msg : str) -> str:
	global chaine
	res = []
	for i in range(len(chaine)):
		res.append( chr( ord(chaine[i]) ^ ord(msg[i]) ) )
	return "".join(res)

msg = get_chaine_from_file("cypher_msg.txt")
print(get_key(msg))

## AVEC LA CLEF TROUVE ##

key = "r3m5-d4yGB"

def cypher(msg : str) -> str:
	global key
	y = 0
	res = []
	for i in msg:
		res.append( chr( ord(i) ^ ord(key[y]) ) )
		y = (y+1) if y < (len(key)-1) else 0
	return "".join(res)

print(cypher(msg))