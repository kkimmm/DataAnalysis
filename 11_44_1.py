import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.start1 = 0
        self.stop1 = 0

    
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    
    #开始计时
    def start(self):
        self.start1 = t.localtime()
        self.prompt = "请先调用 stop() 停止计时"
        print("计时开始")


    #停止计时
    def stop(self):
        if not self.start1:
            print('请先调用 start() 进行计时')
        else:
            self.stop1 = t.localtime()
            self._calc()   #调用内部方法
            print("计时结束")
        

    #内部方法计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop1[index] - self.start1[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
            
      #  print(self.prompt)


