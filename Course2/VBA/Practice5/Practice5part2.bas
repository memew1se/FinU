Attribute VB_Name = "Practice5part2"
Option Explicit


Public Sub task2()

Const N = 3
Const M = 4

ReDim A(N, M) As Integer
ReDim B(M, N) As Integer

Dim i, j As Integer

Randomize
For i = 1 To N
For j = 1 To M
    Cells(i, j) = Int((5 + 5 + 1) * Rnd - 5)
    A(i, j) = Cells(i, j)
    B(j, i) = Cells(i, j)
Next j
Next i


For i = 1 To M
For j = 1 To N
    Cells(i + 4, j) = B(i, j)
Next j
Next i

End Sub
