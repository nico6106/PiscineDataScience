def isNaN(num):
    return num != num

def NULL_not_found(object: any) -> int:
	value=object
	info = type(object)
	if type(object) is None:
		print(f"Nothing: None {info}")
	elif type(object) is float and isNaN(value):
		print(f"Cheese: {value} {info}")
	elif type(object) is int and value == 0:
		print(f"Zero : {value} {info}")
	elif type(object) is str and value == '':
		print(f"Empty : {info}")
	elif type(object) is bool and not value:
		print(f"Fake : {value} {info}")
	else:
		print("Type not found")
		return 1
	return 0