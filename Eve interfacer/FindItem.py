import urllib.request, json 
name = input("What's your name? ")
with urllib.request.urlopen("https://esi.evetech.net/latest/search/?categories=inventory_type&datasource=tranquility&language=en-us&search="+name.replace(" ", "%20")+"&strict=false") as url:
	items = json.loads(url.read().decode())
	if len(items) > 0:
		if len(items['inventory_type']) < 30:
			print(len(items['inventory_type']))
			print(items['inventory_type'][0])
			for item in items['inventory_type']:
				with urllib.request.urlopen("https://esi.evetech.net/latest/universe/types/"+str(item)+"/?datasource=tranquility&language=en-us") as url:
					names = json.loads(url.read().decode())
					print(names['name'])
		else:
			print(len(items['inventory_type']))
			print("Please refine your search")
	else:
		print("Not Found")
