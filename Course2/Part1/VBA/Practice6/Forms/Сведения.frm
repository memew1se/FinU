VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Сведения 
   Caption         =   "UserForm2"
   ClientHeight    =   3015
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4560
   OleObjectBlob   =   "Сведения.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Сведения"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cm_OK_Click()
Dim i As Integer
Sheets(1).Activate
ActiveCell.Offset(1, 0).Activate
i = ActiveCell.Row
' вместо предыдущих двух строк для записи данных в
' ту же книгу можно использовать оператор:
' i = Range("A1").CurrentRegion.Rows.Count + 1
ActiveSheet.Cells(i, 1) = TextBox_clientID
ActiveSheet.Cells(i, 2) = TextBox_ln
ActiveSheet.Cells(i, 3) = TextBox_carID
i = ActiveCell.Row + 1
End Sub

Private Sub cm_exit_Click()
Hide
End Sub


