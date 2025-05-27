questions = [
    "1. What is the name of India’s first nuclear-powered submarine?",
    "2. Who developed India's first supercomputer 'PARAM 8000'?",
    "3. In which year did India conduct its first nuclear test at Pokhran?",
    "4. Who was the first Indian to win the Nobel Prize in Physics?",
    "5. What is the codename of India’s first successful nuclear bomb test?",
    "6. Which Indian scientist is known as the 'Father of Indian Space Program'?",
    "7. Which city is known as the 'Silicon Valley of India'?",
    "8. Which Indian satellite was the first to be placed in orbit?",
    "9. What was the name of the first Indian mission to Mars?",
    "10. Who is the first Indian woman to go to space?",
    "11. Who served as the first Indian Chief of Defence Staff (CDS)?",
    "12. What is the full form of DRDO?",
    "13. Who was the first Indian to receive the Bharat Ratna posthumously?",
    "14. Which Indian mathematician made significant contributions to number theory and died at 32?",
    "15. What was the operation name of India’s surgical strike in 2016?"
]

options = [
    ["A. INS Chakra", "B. INS Arihant", "C. INS Vikrant", "D. INS Shivalik"],
    ["A. Dr. A.P.J. Abdul Kalam", "B. Sam Pitroda", "C. Vijay Bhatkar", "D. Homi Bhabha"],
    ["A. 1971", "B. 1974", "C. 1998", "D. 2001"],
    ["A. Subrahmanyan Chandrasekhar", "B. Homi Bhabha", "C. C.V. Raman", "D. Venkatraman Ramakrishnan"],
    ["A. Smiling Buddha", "B. Trishul", "C. Pokhran-X", "D. Ashvamedha"],
    ["A. Vikram Sarabhai", "B. Homi Bhabha", "C. Satish Dhawan", "D. C.N.R. Rao"],
    ["A. Hyderabad", "B. Mumbai", "C. Bengaluru", "D. Pune"],
    ["A. GSAT-1", "B. Aryabhata", "C. Rohini", "D. INSAT-1A"],
    ["A. Mangalyaan", "B. Chandrayaan-1", "C. Mars Orbiter", "D. Mangala-1"],
    ["A. Sunita Williams", "B. Ritu Karidhal", "C. Kalpana Chawla", "D. Tessy Thomas"],
    ["A. General Bipin Rawat", "B. General V.K. Singh", "C. General Dalbir Singh", "D. General Anil Chauhan"],
    ["A. Defence Research and Development Organization", "B. Directorate of Research and Development Organisation", "C. Department of Research and Defence Operations", "D. Development Research & Defence Order"],
    ["A. C. Rajagopalachari", "B. B.R. Ambedkar", "C. Sardar Patel", "D. Lal Bahadur Shastri"],
    ["A. Aryabhatta", "B. Ramanujan", "C. Harish-Chandra", "D. P.C. Mahalanobis"],
    ["A. Operation Vijay", "B. Operation Meghdoot", "C. Operation Black Tornado", "D. Operation Surgical Strike"]
]

correct_answers = [
    "B", "C", "B", "C", "A",
    "A", "C", "B", "A", "C",
    "A", "A", "D", "B", "D"
]

prize_money = [
    10000, 20000, 40000, 80000, 160000,
    320000, 640000, 1250000, 2500000, 5000000,
    10000000, 15000000, 25000000, 50000000, 70000000
]

earned = 0
print("🎉 Welcome to KBC - Toughest Edition 🎉\n")

for i in range(15):
    print("=" * 60)
    print(questions[i])
    for option in options[i]:
        print(option)
    ans = input("Your answer (A/B/C/D): ").strip().upper()

    if ans == correct_answers[i]:
        earned = prize_money[i]
        print(f"✅ Correct! You have won ₹{earned}\n")
    else:
        print(f"❌ Wrong answer. The correct answer was '{correct_answers[i]}'.")
        print(f"You take home ₹{earned}. Better luck next time!\n")
        break
else:
    print("🏆 Congratulations! You're a true genius!")
    print(f"You have won ₹{prize_money[-1]} – CROREPATI!\n")
