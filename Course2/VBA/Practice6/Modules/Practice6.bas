Attribute VB_Name = "Practice6"
Sub Calculation()
Sheets(3).Activate
Range("A:D").Clear
ActiveSheet.Cells(1, 1) = "ID клиента"
ActiveSheet.Cells(1, 2) = "Фамилия"
ActiveSheet.Cells(1, 3) = "Минут аренды"
ActiveSheet.Cells(1, 4) = "Сумма"
i = 2
j = 2
Do While Sheets(1).Cells(j, 1) <> ""
    ActiveSheet.Cells(i, 1) = Sheets(1).Cells(j, 1)
    ActiveSheet.Cells(i, 2) = Sheets(1).Cells(j, 2)
    ActiveSheet.Cells(i, 3) = InputBox("Время аренды (в минутах)", , "60")
k = 2
Do While Sheets(2).Cells(k, 1) <> ""
    If Sheets(1).Cells(j, 3) = Sheets(2).Cells(k, 1) Then
        ok = Sheets(2).Cells(k, 2)
    End If
    k = k + 1
Loop
    ActiveSheet.Cells(i, 4) = ActiveSheet.Cells(i, 3) * ok / 60
    j = j + 1
    i = i + 1
Loop
End Sub
