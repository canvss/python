# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/23 13:55
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""

# 一张牌
import random


class Card(object):
    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self.face == 1:
            face_str = 'A'
        elif self.face == 11:
            face_str = 'J'
        elif self.face == 12:
            face_str = 'Q'
        elif self.face == 13:
            face_str = 'K'
        else:
            face_str = self.face
        return '%s%s' % (self.suite, face_str)

    def __repr__(self):
        return self.__str__()


# 一副牌
class Poker(object):
    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]

        self._current = 0

    @property
    def cards(self):
        return self._cards

    @property
    def current(self):
        return self.current

    def shuffle(self):
        self._current = 0
        # 将序列中的元素随机排序
        random.shuffle(self._cards)

    @property
    def next(self):
        # 发牌
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        # 还有没有牌
        return self._current < len(self._cards)


class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards_on_hands = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hands(self):
        return self._cards_on_hands

    def get(self, card):
        # 摸牌
        return self.cards_on_hands.append(card)

    # 整理手中的牌
    def arrange(self, card_key):
        self._cards_on_hands.sort(key=card_key)


def get_key(card):
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    player = Player('刘国鹏')
    for _ in range(13):
        player.get(p.next)
    print(player.name + ':', end=' ')
    player.arrange(get_key)
    print(player.cards_on_hands)


if __name__ == '__main__':
    main()
