lst : list = []
lst.append('Krishna')
print(lst)

Attendees = ["battu","shyam", "raj"]
Attendees.insert(1,"samrat")
print(Attendees)

Attendes = ("sam","shyam","raj","samrat","battu")
print(Attendes.count("shyam"))

attendes = ["raj","reena"]
print(attendes.count("sam"))

attendes = ["sam","raj","chinni","mani","lasya"]
print(attendes)

attendees = ["sam","raju","mani","chinnu"]
attendees = ["shyam","samrat","pandu","krishna"]
attendees.extend(attendees)
print(attendees)
print(attendees)

attendees = ["pandu","raju","sravantika","mouni"]
attendees.remove("raju")
print(attendees)

# pop with index
attendees = ["sam","samrat","raj","shyam"]
attendees.pop(1)
print(attendees)

#pop without index :
attendes = ["sam","shyam","naresh","vishnu murthy","krishna murthy"]
attendes.pop()
attendes.pop()
attendes.pop()
print(attendes)
