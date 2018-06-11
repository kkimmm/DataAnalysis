import easygui as g
import sys

while 1 :
        g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")



        choice = ["语文", "英语", "数学", "C++"]
                
        choice = g.choicebox(msg ="你最喜欢的课程？", title = "小游戏互动", choices=choice)

                # note that we convert choice to string, in case
                # the user cancelled the choice, and we got None.
        g.msgbox("你的选择是: " + str(choice), "结果")
        
        if g.ccbox(msg = "你希望重新开始小游戏吗？",  title = "请选择"):
                # show a Continue/Cancel dialog
                g.msgbox('确定')
        else:
                sys.exit(0)     # user chose Cancel

