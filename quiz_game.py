import time

hearts = 3
points = 0

questions = ["What is the capital of Turkey?\n",
             "What is the biggest ocean in the world?\n",
             "What is the symbol of python coding language?\n",
             "What is the speed of light?\n",
             "What is the smallest prime number?\n",
             "Which two seas does the Bosphorus Strait connect?\n",
             "In which year did the first manned moon landing occur?\n",
             "Which scientist discovered that the electron is negatively charged?\n",
             "Which element has the chemical symbol 'O'?\n",
             "How many hours are in a week?\n"]

answers = [["A. Ankara\n","B. Istanbul\n","C. Izmir\n","D. Antalya\n"],
           ["A. Atlantic Ocean\n","B. Indian Ocean\n","C. Pacific Ocean\n","D. Southern Ocean\n"],
           ["A. Lion\n","B. Dog\n","C. Snake\n","D. Sheep\n"],
           ["A. 200,000 km/sec\n","B. 300,000 km/sec\n","C. 450,000 km/sec\n","D. 500,000 km/sec\n"],
           ["A. 5\n","B. 7\n","C. 9\n","D. 2\n"],
           ["A. Aegean and Marmara\n","B. Black Sea and Marmara\n","C. Mediterranean and Black Sea\n","D. Mediterranean and Aegean\n"],
           ["A. 1989\n","B. 1980\n","C. 1970\n","D. 1969\n"],
           ["A. J.J. Thomson\n","B. Friedrich Bergius\n","C. Pierre Curie\n","D. John Dalton\n"],
           ["A. Oxidene\n","B. Nitrogen\n","C. Oxygen\n","D. Sodium\n"],
           ["A. 152 hours\n","B. 158 hours\n","C. 162 hours\n","D. 168 hours\n"]]

correct_answers = ["A", "C", "C", "B", "D", "B", "D", "A", "C", "D"]

print("Welcome to the quiz game!")

while hearts > 0:
    for question_index in range(len(questions)):
        print(questions[question_index])
        print(''.join(answers[question_index]))
        player_answer = input("Answer: ").upper()

        if player_answer == correct_answers[question_index]:
            print("Good job, you earned 10 points!")
            points += 10
        else:
            print("Sorry, wrong answer :(")
            hearts -= 1
        
        print(f"Hearts left: {hearts}")
        
        if hearts == 0:
            print("Sorry, you lost :(")
            time.sleep(1)
            break

print("Game Over!")
