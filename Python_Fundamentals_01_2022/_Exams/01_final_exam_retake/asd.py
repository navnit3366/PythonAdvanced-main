# # a = "0123456789"
# # # a = "Hawai::RomeCyprys-Greece"
# # indx1 = 11
# # indx2 = 10
# #
# # a1 = a[:indx1] + " " + a[indx1:]
# # print(a1)
# # # a2 = a[indx2+1:]
# # #
# # #
# # # a3 = a1 + a2
# # #
# # # print(f"a1({a1}) + a2({a2}) = a3({a3})")
# # b = [1,2]
# # b[0] = 5
# # b[1] = 10
# # print(b)
# a = "0123456789"
# a1 = a[2:(2+3)]
# print(a1)
raw_str = "0123456789"

start_index = 1
end_index = 5
substring = raw_str[start_index:end_index]
new_substring = substring[::-1]
raw_str = raw_str[:start_index] + new_substring + raw_str[end_index:]
print(raw_str)
