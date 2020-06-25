class Get_Score:
    tot = []
    avg = []
    excel = []
    rank = []
    
    def Get_Grade(self):
        fp = open("score.csv","r",encoding = "utf-8")
        self.excel = fp.readlines()
        fp.close()
                  
        for i in range(len(self.excel)):
            std = self.excel[i].split(",") 
            self.tot.append(int(std[2])+int(std[3])+int(std[4]))
            self.avg.append(round(self.tot[i]/3,2))
        
        for score1 in self.tot:
            rk = 1
            for score2 in self.tot:
                if score1 < score2:
                    rk = rk + 1
            self.rank.append(rk)

        fp.close()        
        l = len(self.excel)

        with open("grade.csv","w",encoding = "utf-8") as wr:
            for i in range(l):
                wr.write(self.excel[i].replace('\n','')+',')
                wr.write(' 총점 // ' + self.tot[i].__str__()+',')
                wr.write(' 평균 // ' + self.avg[i].__str__()+',')
                wr.write(' 등수 // ' + self.rank[i].__str__()+'\n')

scr = Get_Score()
scr.Get_Grade()

