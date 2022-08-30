from flatten_json import flatten
import json

with open('resultadoapp2.json') as file:
	with open('flatten.json','a+') as file2:
		j = json.loads(file.read())
		for i in j:
			print(i)
			flat_json = json.dumps(flatten(i))
			file2.write(flat_json + ',')

