Attribute VB_Name = "��������2�����1"
Option Explicit


Public Sub task()

    Dim x, y, z As Long
    
    x = Val(InputBox("������� x"))
    y = Val(InputBox("������� y"))
    z = Val(InputBox("������� z"))
    
    Dim s As Double
    
    s = (z * Sqr(x) - (y ^ 2) * x ^ (1 / 3)) / _
        (x + 0.5) ^ (1 / 5)
    
    MsgBox ("s = " & s)
    
End Sub
    
    
    
Public Sub task2()
    
    Dim g, z As Long
    
    g = Val(InputBox("������� g"))
    z = Val(InputBox("������� z"))
    
    Dim b As Double
    
    b = Cos(g ^ 2 * z ^ (-1))
    
    MsgBox ("b = " & b)

End Sub
