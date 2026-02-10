score = 0

print("LOGICAL REASONING QUIZ")
print("--------------------------------------")

# Question 1
print("\n1. What comes next in the series: 2, 4, 8, 16, ?")
print("A. 18\nB. 24\nC. 32\nD. 64")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 2
print("\n2. Find the odd one out:")
print("A. Dog\nB. Cat\nC. Cow\nD. Lion")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 3
print("\n3. If 3 + 5 = 28, 4 + 6 = 40, then 5 + 7 = ?")
print("A. 48\nB. 60\nC. 70\nD. 84")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "D":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 4
print("\n4. What comes next: A, C, E, G, ?")
print("A. H\nB. I\nC. J\nD. K")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "B":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 5
print("\n5. If ALL BLOOMS are flowers, then BLOOMS are?")
print("A. Trees\nB. Plants\nC. Animals\nD. Birds")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "B":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 6
print("\n6. Find the missing number: 1, 4, 9, 16, ?")
print("A. 20\nB. 24\nC. 25\nD. 36")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 7
print("\n7. Which number does not belong?")
print("A. 2\nB. 3\nC. 5\nD. 9")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "D":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 8
print("\n8. If DAY is coded as 4, NIGHT is coded as?")
print("A. 4\nB. 5\nC. 6\nD. 7")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 9
print("\n9. Which word is opposite of 'Expand'?")
print("A. Increase\nB. Enlarge\nC. Contract\nD. Grow")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct")
    score += 1
else:
    print("Wrong")

# Question 10
print("\n10. What comes next: 3, 6, 11, 18, ?")
print("A. 25\nB. 27\nC. 29\nD. 30")
ans = input("Enter your answer (A/B/C/D): ").upper()
if ans == "C":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("\n--------------------------------------")
print("Quiz Completed")
print("Your Score:", score, "/ 10")
