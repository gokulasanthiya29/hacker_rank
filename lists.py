if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        cmd = input().split()
        # insert
        if cmd[0] == "insert":
            my_list.insert(int(cmd[1]), int(cmd[2]))
        # print
        if cmd[0] == "print":
            print(my_list)
        # remove
        if cmd[0] == "remove":
            my_list.remove(int(cmd[1]))
        # append
        if cmd[0] == "append":
            my_list.append(int(cmd[1]))
        # sort
        if cmd[0] == "sort":
            my_list.sort()
        # pop
        if cmd[0] == "pop":
            my_list.pop(-1)
        # reverse
        if cmd[0] == "reverse":
            my_list.reverse()
                
    
