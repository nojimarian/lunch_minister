"""ランチ大臣の実行クラス"""

from slack import Slack

class LunchMinister:
    """"""

    def __init__(self):
        """なにかやることあるかな"""
        pass

    def lunch_time_now(self):
        """実行関数だよ"""

        message = 'みなさん、ランチの時間ですよ'
        sl_ = Slack()
        sl_.send(message)

        return 0

if __name__ == '__main__':
    lm_ = LunchMinister()
    lm_.lunch_time_now()