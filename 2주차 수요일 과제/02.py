import random


class Character:
    def __init__(self):
        self.name = input('캐릭터의 이름을 입력하세요: ')
        self.str = random.randrange(6, 9)
        self.int = random.randrange(6, 9)
        if self.str > self.int:
            self.job = '전사'
        elif self.str == self.int:
            self.job = '궁수'
        else:
            self.job = '법사'

    def info(self):
        print('캐릭터 이름: {}'.format(self.name))
        print('캐릭터 정보: 힘({}), 지력({})'.format(self.str, self.int))
        print('캐릭터 직업: {}'.format(self.job))


Injun = Character()
Injun.info()

