import time
import random

class 同事报错(Exception):
    def __init__(self, ErrorMessage = "我不清楚"):
        super().__init__(self)
        if isinstance(ErrorMessage, str):
            self.ErrorMessage = ErrorMessage
        else:
            self.ErrorMessage = ErrorMessage.背锅侠 + "说: " + ErrorMessage.遗言
    
    def __str__(self):
        return self.ErrorMessage

class 我的责任(Exception):
    def __init__(self, ErrorMessage = "就算我有 99% 的责任，难道我同事没有 1% 的责任吗"):
        super().__init__(self)
        if isinstance(ErrorMessage, str):
            self.ErrorMessage = ErrorMessage
        else:
            self.ErrorMessage = ErrorMessage.遗言 + " --" + ErrorMessage.背锅侠
    
    def __str__(self):
        return self.ErrorMessage

class 黑锅():
    def __init__(self, 背锅侠 = "新来的", 遗言 = "我对项目不太熟"):
        self.背锅侠 = 背锅侠
        self.遗言 = 遗言
    
    def 同事说过(self):
        raise 同事报错(self)
    
    def 抛出黑锅(self):
        raise 同事报错(self)
    
    def 承担责任(self):
        raise 我的责任(self)

class 跑路(object):
    def __init__(self, 等会儿 = 0):
        if 等会儿 == 0:
            exit()
        else:
            time.sleep(等会儿)
            exit()

class 黑锅处理():
    def __init__(self):
        self.黑锅 = "我来"
    
    def 尝试接锅(self, function):
        def 黑锅销毁(*args, **kwargs):
            try:
                info = function(*args, **kwargs)
            except 同事报错:
                pass
            except 我的责任:
                pass
            else:
                return info
        return 黑锅销毁
    
    def 我来背锅(self, 英雄大名):
        def 换个锅背(function):
            def 创建我的责任(*args, **kwargs):
                try:
                    info = function(*args, **kwargs)
                except:
                    pass
                else:
                    return info
                我的锅 = 黑锅(英雄大名, "出了问题报了错找我，我是写这块代码的")
                我的锅.承担责任()
            return 创建我的责任
        return 换个锅背

class 你说得对():
    def __init__(self):
        self.你说的 = "真对"
    
    def 啊对对对(self, 希望):
        def 滚刀(function):
            def 就是不听(*args, **kwargs):
                if isinstance(希望, list):
                    if 希望[0] == "$":
                        newList = 希望
                        newList.pop(0)
                        return random.choice(newList)
                    else:
                        return 希望
                else:
                    return 希望
            return 就是不听
        return 滚刀

关我屁事 = None
