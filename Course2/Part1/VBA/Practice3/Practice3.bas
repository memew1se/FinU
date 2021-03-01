Attribute VB_Name = "Practice3"
Option Explicit


Public Sub task1()

Dim y, abs_v As Double
Dim x, a As Integer

a = Val(InputBox("¬ведите a"))


For x = 1 To 2 Step 0.2

    abs_v = x - a
    y = 2 * Exp(1) ^ Abs(abs_v)

    MsgBox ("x = " & x & Chr(13) + Chr(10) & "y = " & y)

Next x

End Sub



Public Sub task2()

Dim x, p, i As Long

p = 1
x = Val(InputBox("¬ведите x"))

For i = 1 To x
    p = p * i
Next i

MsgBox ("p = " & p)

End Sub
