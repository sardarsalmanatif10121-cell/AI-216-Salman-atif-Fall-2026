# Input: age, programming score, prerequisite completed
# Processing: check all eligibility conditions
# Output: eligible or not eligible with reasons

# Applicant 1
age = 19
programming_score = 72
prerequisite_completed = True

print("--- Applicant 1 ---")
if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Result: Eligible")
else:
    print("Result: Not Eligible")
    if age < 18:
        print("- Age requirement not met")
    if programming_score < 60:
        print("- Programming score requirement not met")
    if not prerequisite_completed:
        print("- Prerequisite course not completed")

# Applicant 2
age = 18
programming_score = 60
prerequisite_completed = True

print("\n--- Applicant 2 ---")
if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Result: Eligible")
else:
    print("Result: Not Eligible")
    if age < 18:
        print("- Age requirement not met")
    if programming_score < 60:
        print("- Programming score requirement not met")
    if not prerequisite_completed:
        print("- Prerequisite course not completed")

# Applicant 3
age = 17
programming_score = 55
prerequisite_completed = False

print("\n--- Applicant 3 ---")
if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Result: Eligible")
else:
    print("Result: Not Eligible")
    if age < 18:
        print("- Age requirement not met")
    if programming_score < 60:
        print("- Programming score requirement not met")
    if not prerequisite_completed:
        print("- Prerequisite course not completed")