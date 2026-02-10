questions = [
    {"q": "1. What comes next in the series: 2, 4, 8, 16, ?", 
     "opt": ["A. 18", "B. 24", "C. 32", "D. 64"], "ans": "C"},

    {"q": "2. Find the odd one out:", 
     "opt": ["A. Dog", "B. Cat", "C. Cow", "D. Lion"], "ans": "C"},

    {"q": "3. If 3 + 5 = 28, 4 + 6 = 40, then 5 + 7 = ?", 
     "opt": ["A. 48", "B. 60", "C. 70", "D. 84"], "ans": "D"},

    {"q": "4. What comes next: A, C, E, G, ?", 
     "opt": ["A. H", "B. I", "C. J", "D. K"], "ans": "B"},

    {"q": "5. If ALL BLOOMS are flowers, then BLOOMS are?", 
     "opt": ["A. Trees", "B. Plants", "C. Animals", "D. Birds"], "ans": "B"},

    {"q": "6. Find the missing number: 1, 4, 9, 16, ?", 
     "opt": ["A. 20", "B. 24", "C. 25", "D. 36"], "ans": "C"},

    {"q": "7. Which number does not belong?", 
     "opt": ["A. 2", "B. 3", "C. 5", "D. 9"], "ans": "D"},

    {"q": "8. If DAY is coded as 4, NIGHT is coded as?", 
     "opt": ["A. 4", "B. 5", "C. 6", "D. 7"], "ans": "C"},

    {"q": "9. Which word is opposite of 'Expand'?", 
     "opt": ["A. Increase", "B. Enlarge", "C. Contract", "D. Grow"], "ans": "C"},

    {"q": "10. What comes next: 3, 6, 11, 18, ?", 
     "opt": ["A. 25", "B. 27", "C. 29", "D. 30"], "ans": "C"},

    {"q": "11. Which number is a prime number?", 
     "opt": ["A. 9", "B. 15", "C. 21", "D. 17"], "ans": "D"},

    {"q": "12. If CAT = 24, DOG = 26, then BAT = ?", 
     "opt": ["A. 21", "B. 23", "C. 24", "D. 25"], "ans": "C"},

    {"q": "13. Find the odd one:", 
     "opt": ["A. Circle", "B. Square", "C. Triangle", "D. Cube"], "ans": "D"},

    {"q": "14. Which number comes next: 5, 10, 20, 40, ?", 
     "opt": ["A. 60", "B. 70", "C. 80", "D. 90"], "ans": "C"},

    {"q": "15. If all pens are tools and all tools are objects, pens are?", 
     "opt": ["A. Tools", "B. Objects", "C. Both A and B", "D. None"], "ans": "C"},

    {"q": "16. Find the missing letter: B, E, H, K, ?", 
     "opt": ["A. L", "B. M", "C. N", "D. O"], "ans": "B"},

    {"q": "17. What comes next: 1, 1, 2, 3, 5, ?", 
     "opt": ["A. 6", "B. 7", "C. 8", "D. 9"], "ans": "C"},

    {"q": "18. Which is NOT a vowel?", 
     "opt": ["A. A", "B. E", "C. I", "D. Y"], "ans": "D"},

    {"q": "19. If SOUTH becomes NORTH, EAST becomes WEST, then UP becomes?", 
     "opt": ["A. Down", "B. Side", "C. Left", "D. Right"], "ans": "A"},

    {"q": "20. Which number comes next: 100, 90, 80, 70, ?", 
     "opt": ["A. 50", "B. 60", "C. 65", "D. 75"], "ans": "B"},
]

score = 0

print("LOGICAL REASONING QUIZ")
print("--------------------------------------")

for q in questions:
    print("\n" + q["q"])
    for o in q["opt"]:
        print(o)

    user = input("Enter your answer (A/B/C/D): ").upper()

    if user == q["ans"]:
        print("Correct ")
        score += 1
    else:
        print("Wrong ")

print("\n--------------------------------------")
print("Quiz Completed")
print("Your Score:", score, "/", len(questions))
