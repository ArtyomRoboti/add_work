val = int(input("Введите число от 2 до ... "))
list_ = []
begin_val = 2
while begin_val <= val:
    starts_chek = 2
    for i in range(val + 1):
        if begin_val % starts_chek == 0 and begin_val != starts_chek:
            break
        starts_chek += 1
    else:
        list_.append(begin_val)
    begin_val += 1
print(list_)
