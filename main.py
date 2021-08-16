import readJSON
import random as rd


data = readJSON.readjs("data.json")
front = data["front"]  # 开头语
connect = data["connect"]  # 连接词
sentence = data["sentence"]  # 句子
period = data["period"]  # 断句

repeat_time = 2

def randlist(rdlist):
    global repeat_time
    pool = list(rdlist) * repeat_time
    while True:
        rd.shuffle(pool)
        for element in pool:
            yield element


next_sentce = randlist(sentence)
next_period = randlist(period)
next_connect = randlist(connect)


if __name__ == "__main__":
    temp = ""
    temp += front[rd.randint(0, len(front) - 1)]  # 先加入开头语
    temp += "，"

    while len(temp) < 300:
        judge = rd.randint(0, 100)
        if judge < 5:
            temp += next(next_period)  # 有时需要加入一些断句分割段落使得文章更加前言不搭后语
            temp += "，"
        elif judge < 10:  # 加入连接词使得文章更加前言不搭后语
            temp += next(next_connect)
        else:
            temp += next(next_sentce)
            temp += "，"
    temp += next(next_sentce)
    temp += "。"
    print(temp)