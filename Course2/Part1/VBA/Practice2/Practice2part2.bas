Attribute VB_Name = "��������2�����2"
Option Explicit


Public Sub task1()

    Dim x, y, t As Long
    
    x = Val(InputBox("������� x"))
    y = Val(InputBox("������� y"))
    
    If x < y Then t = x: x = y: y = t
    
    MsgBox ("x = " & x & Chr(13) & "y = " & y)

End Sub



Public Sub task2()

    Dim x, y As Integer
    
    x = Val(InputBox("������� x"))
    
    Select Case x
    
    Case Is > 1
        y = x ^ 2 / 2
        
    Case Is <= 1
        y = 2 * x + 3
        
    End Select
    
    MsgBox ("y = " & y)

End Sub
