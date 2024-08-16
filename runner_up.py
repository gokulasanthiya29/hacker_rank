if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # map to list conversion
    score_sheet = list(arr)
    score_sheet.sort(reverse = True)

    for score in range(len(score_sheet)):
        if score_sheet[score] != score_sheet[score+1]:
            runner_up = score_sheet[score+1]
            break
        else:
            continue
    print(runner_up)
