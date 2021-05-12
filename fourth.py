#slicing  

word = "pizza"

print(
"""
Slicing cheat sheet

0   1   2   3   4   5
+---+---+---+---+---+
| p | i | z | z | a |
+---+---+---+---+---+
-5  -4  -3  -2  -1  
"""
)

start = None
while start != "":
        start = (input("\nStart: "))
        
        if start:
            start = int(start)
            
            finish = int(input("Finish: "))

            print("word[", start, ":", finish, "] is", end=" ")
            print(word[start:finish])

input("\n\nPress the enter key to exit.")

#word[0:4] = word[:4]
#word[2:5] = word[2:]

