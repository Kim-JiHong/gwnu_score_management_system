class Score:
    total = []
    avg = []
    excel = []
    rank = []

    def openfile(self):
        fp = open("score.csv", "r", encoding="utf-8")
        self.excel = fp.readlines()
        fp.close()

    def get_score(self):
        for i in range(len(self.excel)):
            student = self.excel[i].split(',')
            kor = int(student[2])
            eng = int(student[3])
            math = int(student[4])
            self.total.append(kor + eng + math)
            self.avg.append(round(self.total[i] / 3, 2))
        
scr = Score()
scr.openfile()
scr.get_score()