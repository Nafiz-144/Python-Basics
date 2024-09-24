lucky_number = [4, 2, 1, 5, 42]
friends = ["Sadman", "Islam", "john", "Oscar", "Don", "Don"]
friends[2] = input("Enter the name :")
friends.extend(lucky_number)
friends.append("coca cola ")
friends.insert(1, "capter")
friends.remove("Don")
# friends.clear
friends.pop()
print(friends.index("Oscar"))
print(friends.count("Don"))
print(friends)
lucky_number.sort()
print(lucky_number)
lucky_number.reverse()
friends2 = friends.copy()
print(friends2)
print(lucky_number)
# Time 1:18:57/4:26:51
