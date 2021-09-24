# coding=UTF-8
name = "ada_lovelace"

print(name.title())
print(name.upper())
print(name.lower())

# ×Ö·û´®
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"
print(message)

#\tÖÆ±í·û   \n»»ÐÐ·û
print("Python")
print("\tPython")
print("languages:\nPython\nC\nJavaScript")

#É¾³ý¿Õ°× ÔÝÊ±É¾³ý£¬Ô­×Ö·û´®»¹ÊÇ´æÔÚ¿Ø¹É
favorite_language =  " python "
favorite_language.rstrip()
print(favorite_language + "1")
print("1" + favorite_language.rstrip()+ "1")
print("1" + favorite_language.lstrip()+ "1")
print("1" + favorite_language.strip()+ "1")




a = "eric"
print("Hello " + a.title() +", would you like to learn some Python \
today?")
print("Hello " + a.upper() +", would you like to learn some Python \
today?")
print("Hello " + a.lower() +", would you like to learn some Python \
today?")


print("Albert Einstein once said,\"A persion who never made a mistake \
never tried anythingnew.\"")

famous_person = "Albert Einstein"
message = "A persion who never mdae a mistake never tried anythingnew"

print (famous_person + " once said,\"" + message +".\"")


a = "   eric      "
print("\t" + a + "\n" + a)
print("\t" + a.lstrip() + "\n" + "\t" + a.rstrip() + "\n" + "\t" \
+ a.strip())
