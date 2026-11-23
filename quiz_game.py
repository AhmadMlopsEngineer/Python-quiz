questions = ("What data type does Python's input() function always return by default?",

&#x20;            "Which planet in our solar system rotates clockwise (backwards compared to most other planets)?",

&#x20;            "In Python, what does items\[::-1] do to a list?",

&#x20;            "What does HTTP stand for in a website address?",

&#x20;            "Which element has the chemical symbol Au on the periodic table?")



options = (("A. Integer", "B. String", "C. Float", "D. Boolean", "E. Tuple"),

&#x20;          ("A. Mars", "B. Jupiter", "C. Venus", "D. Neptune", "E. Saturn"),

&#x20;          ("A. Deletes the last item", "B. Sorts it alphabetically", "C. Reverses the list", "D. Copies only the first item", "E. Doubles every item"),

&#x20;          ("A. HyperText Transfer Protocol", "B. High Tech Transmission Program", "C. Hyperlink Text Terminal Process", "D. Host Transfer Text Protocol", "E. Hyper Terminal Transfer Path"),

&#x20;          ("A. Silver", "B. Aluminium", "C. Gold", "D. Argon", "E. Aureum"))



answers = ("B", "C", "C", "A", "C")

guesses = \[]

score = 0

question\_number = 0

for question in questions:

&#x20;   print("-------------")

&#x20;   print(question)

&#x20;   for option in options\[question\_number]:

&#x20;       print(option)





&#x20;   guess = input("What is the answer?: ").upper()

&#x20;   guesses.append(guess)

&#x20;   if guess == answers\[question\_number]:

&#x20;       score += 1

&#x20;       print("Correct!")

&#x20;   else:

&#x20;       print("Incorrect!")

&#x20;       print(f"The correct answer is {answers\[question\_number]}")

&#x20;   question\_number += 1

print(f"Your score is {score} out of {len(questions)}")

