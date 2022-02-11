magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
i=0
row1sum=0
row2sum=0
row3sum=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square[i]):
        if i==0:
            row1sum=row1sum+magic_square[i][j]
        if i==1:
            row2sum=row2sum+magic_square[i][j]
        if i==2:
            row3sum=row3sum+magic_square[i][j]
        j=j+1
    i=i+1
print(row1sum,row2sum,row3sum,"it is a magic square") 
                                                                                                                                                                                                                                                              



























































 
  




