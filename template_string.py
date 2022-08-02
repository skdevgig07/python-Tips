from string import Template

data = {
	'tk': 'aeioy',
	'xpto': 'blahblah'
}

t = Template("foobar: $tk yoyoyoyoy $xpto hhahahha")

s = t.substitute(**data)

print(s)
