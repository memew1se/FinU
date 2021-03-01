Attribute VB_Name = "Test1"
Option Explicit


Public Sub task_a()

Dim z, x, y As Double

Const a = -1.7
Const b = 2.4

x = (Cos(a) + Exp(b)) / (a - b)
y = Log(b + 2)

z = Exp(x) - Sin(x + y) ^ 2

MsgBox ("z = " & z)

End Sub


Public Sub task_b(x)

Dim y, p As Double

If x >= 0 Then

    y = x ^ (2 / 3) - 1

Else
    
    y = Log(Abs(x))

End If

p = (Log(Abs(y - Sin(y))) - 2) / (Exp(x) + y + Sqr(Abs(y + 1)))

MsgBox ("x = " & x & Chr(13) + Chr(10) & "y = " & y & Chr(13) + Chr(10) & "p = " & p)

End Sub


Public Sub task_c()

Dim z, u, x As Double
Dim j As Integer

Cells(1, 1) = "z"
Cells(1, 2) = "u"

j = 2

For u = -3.39 To 5.86 Step 0.93

    x = Cos(u - 2) ^ 2
    
    If u < 0.1 Then
    
        z = 2 * Cos(u * x)
        
        Cells(j, 1) = z
        Cells(j, 2) = u
    
    ElseIf u <= 2 Then
    
        z = Log(Abs(Cos(u * x)))
        
        Cells(j, 1) = z
        Cells(j, 2) = u
        
    Else
    
        z = x ^ 2 * Cos(u * x)
        
        Cells(j, 1) = z
        Cells(j, 2) = u
        
    End If
    
    j = j + 1
    
    Next u
    
End Sub


Public Sub main()

task_b (-1.2)
task_b (1.2)
task_b (3.2)

End Sub
