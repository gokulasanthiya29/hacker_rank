def percentage(student_marks, query_name):
    for key, value in student_marks.items():
        if key==query_name:
            average = sum(value) / len(value)
    print("{:.2f}".format(average))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    percentage(student_marks, query_name)
