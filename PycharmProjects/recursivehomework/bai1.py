#Tower of hanoi
def DiskMove(n,c1,c2,c3) :
    if n == 1 :
        print("Dia tu coc ",c1,"chuyen sang coc ",c3) ;
    else :
        DiskMove(n-1,c1,c3,c2) ;
        DiskMove(1,c1,c2,c3) ;
        DiskMove(n-1,c2,c1,c3) ;
DiskMove(4,1,2,3) ;
