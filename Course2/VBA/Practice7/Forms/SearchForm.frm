VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} SearchForm 
   Caption         =   "Поиск"
   ClientHeight    =   3015
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4560
   OleObjectBlob   =   "SearchForm.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "SearchForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()

Dim i As Integer
Dim finder As String

i = 2
finder = SearchForm.TextBox1.Text

While finder <> Worksheets(1).Rows(i).Cells(1).Value
    i = i + 1
Wend

Worksheets(1).Rows(i).Select
SearchForm.Hide

Exit Sub
label:
    MsgBox "Не найдено"

End Sub

Private Sub CommandButton2_Click()

Dim i As Integer
Dim finder As String

On Error GoTo label

i = 2
finder = SearchForm.TextBox2.Text

While finder <> Worksheets(1).Rows(i).Cells(2).Formula
    i = i + 1
Wend

Worksheets(1).Rows(i).Select
SearchForm.Hide

Exit Sub
label:
    MsgBox "Не найдено"

End Sub

Private Sub UserForm_Click()

End Sub
