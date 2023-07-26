def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


def get_name(**data):
    return f"This is {data['name']}"


def get_name_2(data):
    return f"This is {data['name']}"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
print(get_name(**{"name": "George", "town": "Sofia", "age": 20}))
print(get_name_2({"name": "George", "town": "Sofia", "age": 20}))
