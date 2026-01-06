questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)
options = (("A. 110 ", "B. 120 ", "C. 116", "D. 35 "),
           ("A. Whale ", "B. Crocodile", "C. Elepahnt ", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Elephant ", "D. Hyrdrogen "),
           ("A. 206", "B. 207 ", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D.  Mars"),
           )

answer= ("C", "D", "A", "A", "B")

guesses = []
score = 0
questions_number = 0

for question in questions:
    print("-"*7)
    print(question)
    for option in options[questions_number]:
        print(option)

    guess = input("Answer (A,B,C,D)").upper
    

    if guess == answer[questions_number]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answer[questions_number]} is the answer.")
    questions_number += 1