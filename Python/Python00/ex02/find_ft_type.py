
def all_thing_is_obj(object: any) -> int:
	info = type(object)
	if type(object) is list:
		print(f"List : {info}")
	elif type(object) is tuple:
		print(f"Tuple : {info}")
	elif type(object) is set:
		print(f"Set : {info}")
	elif type(object) is dict:
		print(f"Dict : {info}")
	elif type(object) is str:
		print(f"Brian is in the kitchen : {info}")
	else:
		print("Type not found")
	return 42
