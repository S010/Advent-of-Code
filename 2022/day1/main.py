data = []
with open("input.txt","r") as file:
    data = file.readlines()  
    
manCal= []
count = 0
for i in data:
    if i != "\n": 
        count += int(i.strip("\n"))
    else:
        manCal.append(count)
        count = 0

manCal.sort(reverse=True)
print(f"Top mans = {manCal[0]}, Sum of Top three = {sum(manCal[0:3])}")