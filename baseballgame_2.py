import random

# 랜덤으로 정답 생성
answer = random.sample(range(1, 10), 3)
print("정답은=", answer)

# 초기화
cnt = 0
guess = []
strikecnt = 0

plyaer1Base = 0
player2Base = 0

tmpPlayer1Ball = 0
tmpPlayer2Ball = 0

cntPlayer1 = 0
cntPlayer2 = 0

# 게임진행
while player1Base == 3 or player2Base == 3:
    strikecnt = 0
    ballcnt = 0
    guess = []

    for i in range(3):
        num = int(input("{}, 1~9까지 숫자를 입력하세요:".format(i)))
        guess.append(num)

        print(guess)

    for i in range(3):
        if guess[i] == answer[i]:
            strikecnt = strikecnt + 1
        elif guess[i] in answer:
            ballcnt += 1
    print("strike = {}, ball = {}".format(strikecnt, ballcnt))

    cnt += 1

    if player1Base < 4:
        if ballcnt > 0:
            player1Base += (ballcnt + tmpPlayer1Ball) / 4
            tmpPlayer1Ball += (ballcnt + tempPlayer1Ball) % 4
        elif strikecnt > 0:
            player1Base += strikecnt
    elif player1Base >= 4:
        cntPlayer1 += player1Base / 4
        player1Base -= 4 * (player1Base / 4)
    elif isPlayer2 == True and isPlayer1 == False:
        if player2Base < 4:
            if ballcnt > 0:
                player2Base += (ballcnt + tmpPlayer2Ball) / 4
                tmpPlayer2Ball += (ballcnt + tempPlayer2Ball) % 4
            elif strikecnt > 0:
                player2Base += strikecnt
        elif player2Base >= 4:
            cntPlayer2 += player2Base / 4
            player2Base -= 4 * (player2Base / 4)


def checkValue():
    # 초기화

    # for i in range(4):
    for i in range(4):
        guess.append(int(qle.text()[i]))
    # num = int(input("{}, 1~9까지 숫자를 입력하세요:".format(i)))
    # self.guess.append(int(self.qle.text()))
    # self.guess = list()
    # print(guess)

    for i in range(4):
        if guess[i] == value[i]:
            strikecnt = strikecnt + 1
        elif guess[i] in value:
            ballcnt += 1

    # self.lbl2.setText(str(self.guess))
# print("{}번 만에 정답".format(cnt))
