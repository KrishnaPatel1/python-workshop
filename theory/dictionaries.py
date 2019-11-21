Person = {
  "name": "John",
  "last_name": "Doe",
  "age": 26,
  "is_concordian": True
}

print(Person["name"])
print(Person["last_name"])
print(Person["age"])
print(Person["is_concordian"])

Person["age"] = Person["age"] + 4
Person["is_concordian"] = False

print(Person["age"])
print(Person["is_concordian"])

# Challenge 1
# Describe what a classroom dictionary would look like
