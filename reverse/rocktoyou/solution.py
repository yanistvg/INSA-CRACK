import subprocess

f = open("/usr/share/wordlists/rockyou.txt", "r", encoding='latin-1')
rockYou = f.readlines()
f.close()

for passwd in rockYou:
	password = passwd.replace("\n", "").replace("\r", "")
	tmp = subprocess.Popen("./files/nothing.bin "+password+" 1", stdout=subprocess.PIPE, shell=True)
	result = tmp.communicate()
	if "INSACRACK{".encode() in result[0]:
		print(password, " -> ", result[0].decode().replace("\n", ""))
		exit()

# $ python3 solution.py 
# sexymama  ->  INSACRACK{R0cK_Y0u_1s_Us3FuLl}

