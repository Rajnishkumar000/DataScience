a = """Lorem ipsum dolor sit amet,consectetur adip
isc
ing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
b = "Hello,World!"
print(b[6])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


##SLICING


  b = "0123456789"
  print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())
print(a)

a = "rajnish,kumar"
b = a.split(",")
print(b)
