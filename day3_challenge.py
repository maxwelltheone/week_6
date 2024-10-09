##################### DAY 3 CHALLENGE########################
# maxwelltheone
# elpancho17
# V
# malik

text = input("Enter and/or type in a text: ").lower() #this will print out the quote and make the whole quote lowercase

letter1 = input("Enter a random letter: ").lower() #letter selection in lowercase
letter2 = input("Enter a random letter: ").lower() #letter selection in lowercase
letter3 = input("Enter a random letter: ").lower() #letter selection in lowercase

new_list = text.split() #splits the text into a list
print(new_list)
print(len(new_list)) #finds the amount of words in the list

first_letter = print(new_list[0][1]) #first letter of text
last_letter = print(new_list[43][7]) #last letter of text

text_tuple= tuple(text) #turns list into tuple
print(text_tuple)

print(text_tuple.count(letter1)) #how many times letter1 is in text
print(text_tuple.count(letter2)) #how many times letter2 is in text
print(text_tuple.count(letter3)) #how many times lettter3 is in text
 
print(new_list[::-1]) #reverses the list 
print(new_list) #Joins list back together

print("python" in new_list) #finds if python is in text
