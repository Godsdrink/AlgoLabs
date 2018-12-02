class FriendScore:
    def highestScore(friends):
        n = len(friends)
        ans = 0

        for i in range(n):
            cnt = 0
            for j in range(n):
                if i == j:
                    continue

                if friends[i][j] == 'Y':
                    cnt = cnt + 1
                else:
                    for k in range(n):
                        if friends[i][k] == 'Y'and friends[j][k] == 'Y':
                            cnt = cnt + 1
                            break
            ans = max(ans, cnt)
        return ans


    print(highestScore(["NYY", "YNY", "YYN"]))
    #print(highestScore(["NYNNN", "YNYNN", "NYNYN", "NNYNY", "NNNYN"]))

