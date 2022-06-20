not_cypher = open("reception_1.txt", "r")
cypher = open("reception_2.txt", "r")

msg_cypher = cypher.read()
msg_not_cypher = not_cypher.read()

not_cypher.close()
cypher.close()

for i in range(len(msg_not_cypher)):
	print( chr(ord(msg_not_cypher[i]) ^ ord(msg_cypher[i])), end="")
print("\n")

key = "mY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3dUr3_x0rmY_S3dUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_x0rmY_S3cUr3_0rmY_S3cUr3_x0rmY_S3dUr3_x0rmY_S3dUr3_x0rmY_S3cUr3_x"

f = open("reception_3.txt")
flag = f.read()
f.close()
y = 0
for i in range(len(flag)):
	print( chr(ord(flag[i]) ^ ord(key[y])), end="")
	y += 1
print()