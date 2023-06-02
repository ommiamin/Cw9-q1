import re

test_string = input('Enter your password :')
pattern = r"(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d]{8,}"
result = re.match(pattern, test_string)

if result:
  print("password successful.")
else:
  print("password unsuccessful.")