Attribute VB_Name = "Практика2часть1"
Option Explicit


Public Sub task()

    Dim x, y, z As Long
    
    x = Val(InputBox("Введите x"))
    y = Val(InputBox("Введите y"))
    z = Val(InputBox("Введите z"))
    
    Dim s As Double
    
    s = (z * Sqr(x) - (y ^ 2) * x ^ (1 / 3)) / _
        (x + 0.5) ^ (1 / 5)
    
    MsgBox ("s = " & s)
    
End Sub
    
    
    
Public Sub task2()
    
    Dim g, z As Long
    
    g = Val(InputBox("Введите g"))
    z = Val(InputBox("Введите z"))
    
    Dim b As Double
    
    b = Cos(g ^ 2 * z ^ (-1))
    
    MsgBox ("b = " & b)

End Sub
