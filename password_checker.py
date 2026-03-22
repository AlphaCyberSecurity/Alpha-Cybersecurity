import re

#ALPHA CYBERECURITY - PASSWORD AUDITOR

COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "admin", "letmein",
    "welcome", "monkey", "dragon", "master", "123456789",
    "password1", "iloveyou", "sunshine", "princess", "football",
    "shadow", "supernam", "michael", "password123", "abc123" 
]

def check_password(password):
    score = 0
    tips = []

    #Rule 1: Length
    if len(password) >= 20:
        score += 4
    elif len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 12 characters - longer is always stronger")
    #Rule 2: Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        tips.append("Add uppercase letters A through Z")
    #Rule 3: Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        tips.append("Add lowercase letters a through z")
    #Rule 4: Numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        tips.append("Add number 0 through 9")
    #Rule 5: Special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}:;,.<>?]', password):
        score += 2
    else:
        tips.append("Add special characters like !@#$%^&*")
    #Rule 6: NO repeated charcters
    if not re.search(r'(.)\1{2,}', password):
        score += 1
    else:
        tips.append("Avoid repeating the same character 3 or more times")
    #Check against common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips = ["CRITIAL: This is one of the most commonly hacked passwordsin the world. Change it immediately."]
    #Convert score to rating
    if score >= 8:
        rating = "EXCELLENT"
        colour = "[PASS]"
    elif score >= 6:
        rating = "STRONG"
        colour = "[PASS]"
    elif score >= 4:
        rating = "GOOD"
        colour = "[WARN]"
    elif score >= 2:
        rating = "WEAK"
        colour = "[FAIL]"
    else:
        rating = "CRITICAL - CHANGE NOW!!"
        colour = "[!!!]"

    print("\n" + "=" * 45)
    print(f" {colour} RATING: {rating}")
    print(f" SCORE: {score} out of 10")
    print("=" * 45)

    if tips:
        print(" HOW TO IMPROVE:")
        for t in tips:
            print(f"    --> {t}")
    else:
        print("This is a strong password. Well done.")
    print()

#Main
print("=" * 45)
print(" ALPHA CYBERSECURITY - PASSWORD AUDITOR")
print("=" * 45)
print(" Test passwords for strength and security.")
print(" Type quit to exit. \n")

while True:
    pw = input(" Enter password to check: ")
    if pw.lower == "quit":
        print("\n Auditor closed. Stay secure.")
        break
    check_password(pw)