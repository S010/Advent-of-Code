commands = []
y = 0 
x = 0
aim = 0

with open("input.txt","rt") as file:
  for i in file.readlines():
    commands.append(str(i.strip("\n")))

for i in commands:
  command = i.split(" ")
  direction = command[0]
  amount = int(command[1])
  if direction == "forward":
    y += amount
    x += aim*amount
  elif direction == "down":
    aim += amount
  elif direction == "up":
    aim -= amount
    
print(f"Result : {int(x)*int(y)}")