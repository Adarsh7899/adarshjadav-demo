import time
import random


def get_divisor(n):
    '''
    随机获得一个数n的整数除数。
    :param n: 一个整数
    :return: 一个数n的整数除数
    '''
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return random.choice(l)


if __name__ =='__main__':
    ops = ['+', '-', '*', '/']
    start_time = time.time()
    total = 0
    correct = 0
    questions = []
    while time.time() - start_time <= 60:
        a = random.randint(1, 99)
        op = random.choice(ops)
        if op == '/':
            # 如果是除法，b为a的一个随机整数除数
            b = get_divisor(a)
        else:
            b = random.randint(1, 99)
        # 正确答案
        a_op_b = '{}{}{}'.format(a, op, b)
        c = int(eval(a_op_b))

        # 让用户输入答案
        try:
            ans = int(input('{} = '.format(a_op_b)))
        except:
            ans = ''

        # 检查是否正确
        if time.time() - start_time <= 60:
            if c == ans:
                print('正确！剩余时间{}秒。'.format(int(60 - (time.time() - start_time))))
                correct = correct + 1
            else:
                print('错误！剩余时间{}秒。'.format(int(60 - (time.time() - start_time))))
            total = total + 1
            questions.append('{}={}'.format(a_op_b, ans))

    print('{}道题目，正确率 {:.2f}%。'.format(total, correct / total * 100))
    for q in questions:
        print(q)
