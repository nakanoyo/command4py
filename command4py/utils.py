def eliminate_none_items(d: dict):
	res = {}
	for key, value in d.items():
		if value == None:
			continue
		res[key] = value
	return res