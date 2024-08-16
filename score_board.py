def nested_lists(score_board):
    scores = []
    for i in score_board:
        scores.append(i[1])
    sorted_scores = set(sorted(scores))
    # get second lowest score
    second_lowest = sorted_scores[1]
    
    names = []
    for i in score_board:
        if i[1] == second_lowest:
            names.append(i[0])
    return sorted(names)

if __name__=="__main__":
    score_board = []
    for _ in range(int(input()):
        name = input()
        score = float(input())
        score_board = l1.append([name, score])
    # function call
    nested_lists(score_board)
