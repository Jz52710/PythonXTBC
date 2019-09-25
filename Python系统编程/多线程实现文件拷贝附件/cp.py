from threading import Thread
import os
class Mymove(Thread):
    def __init__(self):
        super(Mymove,self).__init__()
    def moveOpen(self,moveMkdir,moveName):
        newMoveName = moveName+'-副本'
        if not os.path.exists(newMoveName):
            os.mkdir(newMoveName)#创建目录
        moveNameList = os.listdir(moveName)#返回目录所有文件和目录名
        print(moveNameList)
        for i in moveNameList:
            # if not os.path.exists(i):
            #     self.moveCp(moveMkdir,moveName,newMoveName,i)
            # else:
            #     j = os.listdir(i)
            #     for m in j:
            #         self.moveCp(moveMkdir,moveName,newMoveName,m)
            self.moveCp(moveMkdir, moveName, newMoveName, i)
    def moveCp(self,moveMkdir,moveName,newMoveName,fileName):
        with open(moveMkdir+'\\'+moveName+'\\'+fileName,'r',encoding='utf-8') as f:
            copy = f.read()
        with open(moveMkdir+'\\'+newMoveName+'\\'+fileName,'w') as f:
            f.write(copy)


if __name__ == "__main__":
    for i in range(3):
        cp = Mymove()
        cp.start()
    moveMkdir = os.getcwd()#当前路径
    # print(moveMkdir)
    cp = Mymove()
    cp.moveOpen(moveMkdir,'jz')