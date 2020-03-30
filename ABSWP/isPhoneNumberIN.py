def isPhonenumberIN(num):
    if len(num) != 13 :
        return False
    if num[0:3] != "+91":
        return  False
    if not num[3:13].isdecimal():
        return False
    return True
message = "On my wall i found some writen number +918108855425 and 913215854512"
for i in range(len(message)):
    part = message[i:i+13]
    if isPhonenumberIN(part):
        print("Phonenumber found: " +part )
print("Done")

print(isPhonenumberIN("+918108855425"))
print(isPhonenumberIN("+91ahaahahahah"))
print(isPhonenumberIN("+45878787878787"))
print(isPhonenumberIN("+91810885542"))
print(isPhonenumberIN("+918108855425h"))
print(isPhonenumberIN("+91810885a425"))