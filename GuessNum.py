import random
name = input('您的大名是？')
print('您好，' + name + '！我们来玩儿猜数字游戏吧！')
minNum = int(input('请输入一个最小值：'))
maxNum = int(input('再输入一个最大值：'))
secret = random.randint(minNum, maxNum)
guess = 0
tries = 0
while guess != secret and tries < 5:
    guess = int(input('猜数字游戏开始，请输入数字：'))
    if guess > secret:
        print('您输入的数字大了！')
    elif guess < secret:
        print('您输入的数字小了！')
    tries += 1
    print('这是您第' + str(tries) + '次尝试！')
if guess == secret:
    print('恭喜，您猜对了！')
    print('游戏结束，再见！^_^')
else:
    print('哦哟，机会用完了，下次再来吧！')
