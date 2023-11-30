def average():
    get_score = int(input("Enter the score: "))
    final_score = (get_score / 30) * 100    #in this particular instance, the test has got a maximum of 30 points.
    return final_score

score = average()
print("Final Score:", score)
