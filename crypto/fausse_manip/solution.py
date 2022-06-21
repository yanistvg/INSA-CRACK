cipher = "jILRCGPB@Hqh]R_uP5rSB1p_Pj!yD)u}"

cipher = cipher[::-1][1:]
key = "}"

msg = []
msg.append(key)

for i in range(len(cipher)):
	msg.append(chr(ord(cipher[i]) ^ (ord(key) % (31-i) )))
	key = msg[i+1]

print(''.join(msg[::-1][1:]))