import re,socket

host = "number.quals.seccon.jp"
port = 31337
bot = socket.socket(socket.AF_INET , socket.SOCK_STREAM);
bot.connect((host,port))
lol = 0
while(1):
	dat = bot.recv(10000)
	print dat
	k = dat.split("\n")
	numbers = k[0]
	numbers = numbers.replace(" ","")
	p = numbers.split(",")
	l = []
	for a in p:
		a = a.replace(" ","")
		try:
			c = int(a)
		except:
			pass
		l.append(c)

	if "min" in dat:
		bot.send(str(min(l)))
	else:
		bot.send(str(max(l)))
