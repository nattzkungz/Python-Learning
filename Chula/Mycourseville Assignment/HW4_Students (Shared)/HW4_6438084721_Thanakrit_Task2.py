import numpy as np
## Function
def readfile(path): return np.array([_.strip("\n").strip("\ufeff").split(",") for _ in open(path,"r").readlines()])
def sum_scores(array): return np.sum(np.array(array, dtype='i'), axis=1)

## File Handler
raw_data = readfile("scores_utf8.csv")
# raw_data = readfile(datapath + "scores_correct_utf8.csv") # For testcase checking only

## Main Process
sum_of_score, total_score_given = sum_scores(raw_data[1:,1:4]), sum_scores(raw_data[1:,4:])
score_diff = np.array(np.abs(sum_of_score - total_score_given))
all_total_score_correct = np.array_equal(sum_of_score, total_score_given)
if all_total_score_correct:
    print("*"*28 + "\nThe total scores are correct\n" +"*"*28)
else:
    item_location = []
    print("The following students' total score are incorrect\n" + "*"*56)
    for i in score_diff:
        c = 0
        if i != 0: 
            location = int(np.where(score_diff==i)[0][c])
            if location in item_location: 
                c += 1
            else: item_location.append(location)
    for i in item_location:
        print(f"{str(raw_data[i+1][0])}'s score is {float(score_diff[i])} different from the actual total score")
        print(f"The incorrect total score is {raw_data[i][-1]}")
        print(f"The actual score should be {sum_of_score[i]}\n")
