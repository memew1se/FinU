VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} EditForm 
   Caption         =   "Редактирование"
   ClientHeight    =   4335
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   5745
   OleObjectBlob   =   "EditForm.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "EditForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub AddButton_Click()

Worksheets(1).Rows(EditForm.EndFind).Select
EditForm.TextBox1.Text = ""
EditForm.TextBox2.Text = ""
EditForm.TextBox3.Text = ""

End Sub

Private Sub EditButton_Click()

m = ActiveCell.Row

Worksheets(1).Cells(m, 1).Value = TextBox1.Text
Worksheets(1).Cells(m, 2).Value = TextBox2.Text
Worksheets(1).Cells(m, 3).Value = TextBox3.Text

End Sub

Public Function EndFind()

Dim i As Byte

i = 2

While Worksheets(1).Rows(i).Cells(2).Formula > ""
    i = i + 1
Wend

EndFind = i

End Function

Private Sub SpinButton1_SpinDown()

i = ActiveCell.Row + 1

If Worksheets(1).Rows(i).Cells(1).Value <> "" Then
Worksheets(1).Rows(i).Select

EditForm.TextBox1.Text = Worksheets(1).Rows(i).Cells(1).Value
EditForm.TextBox2.Text = Worksheets(1).Rows(i).Cells(2).Value
EditForm.TextBox3.Text = Worksheets(1).Rows(i).Cells(3).Value
End If
End Sub

Private Sub SpinButton1_SpinUp()

i = ActiveCell.Row - 1

If i >= 2 Then
Worksheets(1).Rows(i).Select

EditForm.TextBox1.Text = Worksheets(1).Rows(i).Cells(1).Value
EditForm.TextBox2.Text = Worksheets(1).Rows(i).Cells(2).Value
EditForm.TextBox3.Text = Worksheets(1).Rows(i).Cells(3).Value
End If
End Sub


