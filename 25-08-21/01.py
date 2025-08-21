name = "Zeeshan"

shortName = name[0:3]  # "name[0:3]" Prints "Zee"
print(shortName)
print(name[:3])
print(name[3:])
print(name[-3:])
print(len(name))
print(name.endswith("an"))
print(name.startswith("an"))
print(name.capitalize())

print(f"Hello {name}, your short name is {shortName}!")


letter = """Dear <Name>,
You are selected!
<Date>"""
print(letter.replace("<Name>",name).replace("<Date>", "25-08-2021"))

print(letter.find('are'))

# 1:50:55