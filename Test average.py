def average():
    get_score = int(input("Enter the score: "))
    Total_questions = int(input("Enter the total number of questions: "))
    final_score = (get_score / Total_questions) * 100    #in this particular instance, the test has got a maximum of 30 points.
    return final_score

score = average()
print("Final Score:", score)
