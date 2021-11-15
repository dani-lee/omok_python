import sys

from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from _ast import Or
from bokeh.core.query import OR


form_class = uic.loadUiType("pyomok02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.reset)
        self.arr2d = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]
        
        self.pb2d = []
        self.flag_bw = True
        self.flag_ing = True
        
        for i in range(10):
            line = []
            for j in range(10):
                self.arr2d[i][j] = 0
                pb_one = QPushButton("",self)
                pb_one.setIcon(QtGui.QIcon('0.png'))
                pb_one.setIconSize(QtCore.QSize(40,40))
                pb_one.setGeometry(QtCore.QRect(j*40+30, i*40+60, 40, 40))
                pb_one.setToolTip("{},{}".format(i,j))
                pb_one.clicked.connect(self.myClick)   
                line.append(pb_one)
            self.pb2d.append(line)
            
        self.myrender()
    
        
    def reset(self):
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j] = 0
        self.myrender()
        self.flag_bw = True
        self.flag_ing = True
    
    def myClick(self):
        if not self.flag_ing:
            return 
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(',')
        x = int(arr_ij[0])
        y = int(arr_ij[1])
        
        if self.arr2d[x][y] > 0 :
            return
        
        stone = -1
        
        if self.flag_bw :
            self.arr2d[x][y] = 1
            stone = 1
        else :
            self.arr2d[x][y] = 2
            stone =2
            
        up = self.checkUP(x,y,stone)
        dw = self.checkDW(x,y,stone)
        ri = self.checkRI(x,y,stone)
        le = self.checkLE(x,y,stone)
        
        ul = self.checkUL(x,y,stone)
        ur = self.checkUR(x,y,stone)
        dl = self.checkDL(x,y,stone)
        dr = self.checkDR(x,y,stone)

        print("up",up)
        print("dw",dw)
        print("ri",ri)
        print("le",le)
        print("ul",ul)
        print("ur",ur)
        print("dl",dl)
        print("dr",dr)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flag_ing = False
            if stone == 1:
                stone_cl = "검은돌"
            else:
                stone_cl = "하얀돌"
            QMessageBox.about(self,'결과',"{}이 승리하였습니다".format(stone_cl))
            
        self.flag_bw = not self.flag_bw
        
        # if up >= 4 or dw >= 4 or ri >= 4 or le >= 4 or ul >= 4 or ur >= 4 or dl >= 4 or dr >= 4 :
        #     if stone == 1:
        #         stone_cl = "검은돌"
        #     else:
        #         stone_cl = "하얀돌"
        #     QMessageBox.about(self,'결과',"{}이 승리하였습니다".format(stone_cl))
        
    def checkDW(self,x,y,stone):
        cnt = 0
        try:
            while True:
                x += 1
                if x < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkUP(self,x,y,stone):
        cnt = 0
        try:
            while True:
                x -= 1
                if x < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkRI(self,x,y,stone):
        cnt = 0
        try:
            while True:
                y += 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkLE(self,x,y,stone):
        cnt = 0
        try:
            while True:
                y -= 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkUL(self,x,y,stone):
        cnt = 0
        try:
            while True:
                x -= 1
                y -= 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkUR(self,x,y,stone):
        cnt = 0
        try:
            while True:
                x -= 1
                y += 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDL(self,x,y,stone):
        cnt = 0
        try:
            while True:
                x += 1
                y -= 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDR(self,x,y,stone):
        cnt = 0
        try:
            while True:
                x += 1
                y += 1
                if x < 0:
                    return cnt
                if y < 0:
                    return cnt
                if self.arr2d[x][y] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0 :
                        self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2d[i][j] == 1 :
                        self.pb2d[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2d[i][j] == 2 :
                        self.pb2d[i][j].setIcon(QtGui.QIcon('2.png'))
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
        
    

        


    