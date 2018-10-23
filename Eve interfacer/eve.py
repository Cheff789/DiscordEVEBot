import urllib.request, json 

f = open("Regions.txt", "w")

with urllib.request.urlopen("https://esi.evetech.net/latest/universe/regions/?datasource=tranquility") as url:
	Regions = json.loads(url.read().decode())
	for Region in Regions:
		with urllib.request.urlopen("https://esi.evetech.net/latest/universe/regions/"+str(Region)+"/?datasource=tranquility&language=en-us") as url:
			sysinfo = json.loads(url.read().decode())
			f.write(sysinfo['name'] +":"+str(Region)+'\n')
			print(sysinfo['name'] +":"+str(Region))
f.close()