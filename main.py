import random

n = int(input("Enter the Length of the password: "))
m = int(input("Enter the Number of Digits in password: "))
l = int(input("Enter the Number of Special Characters in password: "))

if ((m > n) or (l > n)):
  print("Invalid Input")
else:

  password = ""

  alpha = [
      "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
      "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
      "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
      "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
  ]

  spec = [
      "!", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",", "-", ".", "/",
      ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|",
      "}", "~"
  ]

  for j in range(n - (m + l)):
    password = password + (random.choice(alpha))

  for i in range(m):
    password = password + str(random.randint(0, 9))

  for k in range(l):
    password = password + str(random.choice(spec))

  password = "".join(random.sample(password, len(password)))
  print("Your Password is: ", password)
