import urllib.request, json 

f = open("systemsInfo.txt", "w")

with urllib.request.urlopen("https://esi.evetech.net/latest/universe/systems/?datasource=tranquility") as url:
	Systems = json.loads(url.read().decode())
	for sys in Systems:
		with urllib.request.urlopen("https://esi.evetech.net/latest/universe/systems/"+str(sys)+"/?datasource=tranquility&language=en-us") as url:
			sysinfo = json.loads(url.read().decode())
			f.write(sysinfo['name'] +":"+str(sys)+'\n')
			print(sysinfo['name'] +":"+str(sys))
f.close()