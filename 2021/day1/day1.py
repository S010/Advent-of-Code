numbers = []
count = 0
with open("input.txt","rt") as file:
  for i in file.readlines():
    numbers.append(int(i.strip("\n")))
  
counter = 0
counter_two =0
temp = 0
first_line = True
for i in range(len(numbers)):
  if first_line:
    print(f"{i} has no previous numbers")
    first_line = False
  else:
    if numbers[i] > temp:
      print(f"{numbers[i]} (increased) {counter}")
      counter += 1
    else:
      print(f"{i} (decreased)")
    temp = numbers[i]

first_line = True

for i in range(len(numbers)):
  if first_line == True:
    first_line = False
  else:
    if i > 2:
      if numbers[i] > numbers[i-3]:
        counter_two +=1 
    


print(f"Counter 1 = {counter}")
print(f"Counter 2 = {counter_two}")
