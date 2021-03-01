Attribute VB_Name = "Practice4"
Option Explicit


Public Sub task()

Dim i, j, c, r, r2, r3 As Integer
Dim tax As Double
Dim d, d2, d3 As Range

Set d = Worksheets("Лист1").Range("A1").CurrentRegion
r = d.Rows.Count
c = d.Columns.Count

Set d2 = Worksheets("Лист2").Range("A1").CurrentRegion
r2 = d2.Rows.Count

Set d3 = Worksheets("Лист3").Range("A1").CurrentRegion
r3 = d3.Rows.Count


For i = 1 To r3
    d3.Cells(i, 2) = 0
Next i


For i = 1 To r


    For j = 1 To r2
        If d.Cells(i, 2) = d2.Cells(j, 1) Then
            tax = d2.Cells(j, 2)
        End If
    Next j


    For j = 1 To r3
        If d.Cells(i, 2) = d3.Cells(j, 1) Then
            d3.Cells(j, 2) = d3.Cells(j, 2) + tax * d.Cells(i, 3) * d.Cells(i, 4)
        End If
    Next j


d.Cells(i, 5) = tax * d.Cells(i, 3) * d.Cells(i, 4)

Next i
End Sub

