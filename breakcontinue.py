#break statement - stopping a loop

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

#Continue statement- skips a given loop condition

devices = ["laptop", "phone", "tablet"]
for x in devices:
    if x == "phone":
        continue
    print(x)
