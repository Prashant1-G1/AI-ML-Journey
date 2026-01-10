def score(dice):
    score={}
    total=0
    for x in dice:
        score[x]=score.get(x,0)+1
    for num in dice:
        if score[num]>=3:
            if num == 1:
                total+=1000
                score[num]=score[num]-3
            elif num ==6:
                total+=600
                score[num]=score[num]-3
            elif num ==5:
                total+=500
                score[num]=score[num]-3
            elif num ==4:
                total+=400
                score[num]=score[num]-3
            elif num ==3:
                total+=300
                score[num]=score[num]-3
            elif num ==2:
                total+=200
                score[num]=score[num]-3
            else:
                total+=0
    total+=score.get(1,0)*100
    total+=score.get(5,0)*50
    return total