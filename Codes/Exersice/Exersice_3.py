questions = [
    "1. What is the capital of India?",
    "2. How many days are there in a leap year?",
    "3. Which planet is known as the 'Red Planet'?",
    "4. Who wrote the national anthem of India?",
    "5. Which festival is known as the 'Festival of Lights'?",
    "6. Which gas is most abundant in Earth's atmosphere?",
    "7. Who is the author of 'Wings of Fire'?",
    "8. In which year did India gain independence?",
    "9. Which of the following rivers originates from Tibet?",
    "10. Where is the headquarter of ISRO located?",
    "11. Which Indian freedom fighter founded the Indian Home Rule League?",
    "12. What is the scientific name of the human being?",
    "13. Which Mughal emperor built the Jama Masjid in Delhi?",
    "14. Who became the first Indian to win a Nobel Prize?",
    "15. Which Indian satellite was the first to be placed in orbit?"
]

options = [
    ["A. Mumbai", "B. Kolkata", "C. Delhi", "D. Chennai"],
    ["A. 365", "B. 366", "C. 364", "D. 367"],
    ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"],
    ["A. Rabindranath Tagore", "B. Bankim Chandra", "C. Mahatma Gandhi", "D. Subhas Bose"],
    ["A. Holi", "B. Dussehra", "C. Diwali", "D. Raksha Bandhan"],
    ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
    ["A. Abdul Kalam", "B. Ratan Tata", "C. C.V. Raman", "D. Narayana Murthy"],
    ["A. 1946", "B. 1947", "C. 1950", "D. 1948"],
    ["A. Ganga", "B. Yamuna", "C. Brahmaputra", "D. Narmada"],
    ["A. Mumbai", "B. Bengaluru", "C. Delhi", "D. Chennai"],
    ["A. Subhas Chandra Bose", "B. Gandhi", "C. Bal Gangadhar Tilak", "D. Nehru"],
    ["A. Homo erectus", "B. Homo sapiens", "C. Australopithecus", "D. Neanderthal"],
    ["A. Akbar", "B. Babur", "C. Shah Jahan", "D. Aurangzeb"],
    ["A. C.V. Raman", "B. Rabindranath Tagore", "C. Mother Teresa", "D. Amartya Sen"],
    ["A. INSAT-1A", "B. GSAT-1", "C. Aryabhata", "D. Rohini"]
]

correct_answers = ["C", "B", "A", "A", "C", "C", "A", "B", "C", "B", "C", "B", "C", "B", "C"]

prize_money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
               640000, 1250000, 2500000, 5000000, 70000000]

earned = 0
print("🎉 Welcome to KBC (Kaun Banega Crorepati) 🎉\n")

for i in range(15):
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
    print("🎊 Congratulations! You are a Crorepati! 🎊")
    print(f"You have won the grand prize of ₹{prize_money[-1]}!\n")