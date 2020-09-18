Attribute VB_Name = "Практика1часть1"
Option Explicit


Public Sub task1()
    
    Dim x1 As Long

    x1 = InputBox("Введите первое число", "Первое окно", 1)
    
    Dim x2 As Long
    
    x2 = InputBox("Введите второе число", "Второе окно", 2)

End Sub



Public Sub task2()

    Dim Name As String
    
    Name = InputBox("Введите имя", , "Марк")
    
    MsgBox "Привет, " + Name + "!"

End Sub
