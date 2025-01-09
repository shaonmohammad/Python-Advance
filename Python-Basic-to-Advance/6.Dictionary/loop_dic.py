dummy_dict = {
    "name": "John Doe",
    "age": 30,
    "is_active": True,
    "hobbies": ["reading", "cycling", "gardening"],
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "zip_code": "12345"
    },
    "scores": [95, 87, 78, 92],
    "profile": None,
    "is_subscribed": False,
}

print(dummy_dict.keys())
for k in dummy_dict.keys():
    print(k)


print(dummy_dict.values())
for v in dummy_dict.values():
    print(v)

print(dummy_dict.items())
for k,v in dummy_dict.items():
    print(k,v)