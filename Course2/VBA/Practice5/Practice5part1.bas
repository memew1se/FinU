Attribute VB_Name = "Practice5part1"
Option Explicit


Public Sub task1()

Dim A(20) As Integer
Dim i As Integer
Dim sum As Integer
Dim max As Integer

Randomize
For i = 1 To 20
    Cells(1, i) = Int((10 + 10 + 1) * Rnd - 10)
    A(i) = Cells(1, i)
Next i

' “.к. массив заполн€етс€ случайными числами из диапозона [-10;10]
' то изначальный максимум можем об€вить как -11
max = -11

For i = 1 To 20
    If A(i) < 0 Then
        sum = sum + A(i)
    End If
    If A(i) Mod 2 = 0 And A(i) > max Then
        max = A(i)
    End If
Next i

Cells(3, 1) = "sum"
Cells(3, 2) = sum

Cells(4, 1) = "max"

If max = -11 Then
    Cells(4, 2) = "„етный элементов в массиве нет"
Else
    Cells(4, 2) = max
End If


End Sub
 
