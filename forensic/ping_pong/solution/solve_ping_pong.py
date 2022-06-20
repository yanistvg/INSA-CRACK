import codecs

file = open("out.txt")
#sudo tcpdump -r ping_pong.pcap icmp -v | grep ttl
chaine = ""
i = 0
for l in file:
	if i%2 == 0:
		chaine += l.split("ttl ")[1].split(",")[0] + " "

	i+=1

new_chaine = ""
for l in chaine.split(" "):
	if len(l)>1:
		new_chaine += chr(int(l))
new_chaine = bytes.fromhex(new_chaine.replace(" ", "")).decode('utf-8')
print(new_chaine)