import random
import math

# 랜덤으로 정답 생성
# answer = random.sample(range(1,10),4)
# print("정답은=", answer)

# 초기화
cnt = 0
guess = []
strikecnt = 0

isPlayer1 = True
isPlayer2 = False

player1Base = 0
player2Base = 0

tmpPlayer1Ball = 0
tmpPlayer2Ball = 0

cntPlayer1 = 0
cntPlayer2 = 0

# 게임진행
while cntPlayer1 < 3 and cntPlayer2 < 3:
    strikecnt = 0
    ballcnt = 0
    guess = []

    answer = random.sample(range(1, 10), 4)
    print("정답은=", answer)

    for i in range(4):
        input_num = int(input("{}, 1~9까지 숫자를 입력하세요:".format(i)))
        guess.append(input_num)

    for i in range(4):
        if guess[i] == answer[i]:
            strikecnt = strikecnt + 1
        elif guess[i] in answer:
            ballcnt += 1

    print("strike = {}, ball = {}".format(strikecnt, ballcnt))

    if isPlayer1 == True:
        if tmpPlayer1Ball + ballcnt > 0 or strikecnt > 0:
            if (tmpPlayer1Ball + ballcnt) / 4 > 0:
                player1Base += math.trunc((tmpPlayer1Ball + ballcnt) / 4)
                # print("베이스 : {}".format(player1Base))
                tmpPlayer1Ball = (tmpPlayer1Ball + ballcnt) % 4
            if strikecnt > 0:
                player1Base = + strikecnt
            if player1Base >= 4:
                cntPlayer1 += math.trunc(player1Base / 4)
                player1Base = player1Base % 4

        print("Player1 -> 베이스 = {:g}, 스트라이크 = {:g}, 볼 = {:g}, stack_볼 = {:g},  점수 = {:g}".format(
            player1Base, strikecnt, ballcnt, tmpPlayer1Ball, cntPlayer1))
        isPlayer1 = False
        isPlayer2 = True
    elif isPlayer2 == True:
        if tmpPlayer2Ball + ballcnt > 0 or strikecnt > 0:
            if (tmpPlayer2Ball + ballcnt) / 4 > 0:
                player2Base += math.trunc((tmpPlayer2Ball + ballcnt) / 4)
                # print("베이스 : {}".format(player1Base))
                tmpPlayer2Ball = (tmpPlayer2Ball + ballcnt) % 4
            if strikecnt > 0:
                player2Base = + strikecnt
            if player2Base >= 4:
                cntPlayer2 += math.trunc(player2Base / 4)
                player2Base = player2Base % 4

        print("Player2 -> 베이스 = {:g}, 스트라이크 = {:g}, 볼 = {:g}, stack_볼 = {:g},  점수 = {:g}".format(
            player1Base, strikecnt, ballcnt, tmpPlayer1Ball, cntPlayer1))
        isPlayer1 = True
        isPlayer2 = False

    if cntPlayer1 == 3:
        print("player1이 승리하였습니다.")
    elif cntPlayer2 == 3:
        print("player2가 승리하였습니다.")

#     if player1Base < 4:
#         if ballcnt > 0:
#             player1Base += (ballcnt + tmpPlayer1Ball)/4
#             tmpPlayer1Ball += (ballcnt + tmpPlayer1Ball)%4
#         elif strikecnt > 0:
#             player1Base += strikecnt


#     elif player1Base >= 4 and :
#         cntPlayer1 = cntPlayer1 + player1Base/4
#         player1Base -= 4*(player1Base/4)


#     elif isPlayer2 == True and isPlayer1 == False:
#         if player2Base < 4:
#             if ballcnt > 0:
#                 player2Base += (ballcnt + tmpPlayer2Ball) / 4
#                 tmpPlayer2Ball += (ballcnt + tmpPlayer2Ball) % 4
#             elif strikecnt > 0:
#                 player2Base += strikecnt
#         elif player2Base >= 4:
#             cntPlayer2 += player2Base / 4
#             player2Base -= 4 * (player2Base / 4)


# print("{}번 만에 정답".format(cnt))
