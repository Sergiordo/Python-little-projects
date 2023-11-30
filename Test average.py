def average():
    get_score = int(input("Enter the score: "))
    final_score = (get_score / 30) * 100
    return final_score

score = average()
print("Final Score:", score)