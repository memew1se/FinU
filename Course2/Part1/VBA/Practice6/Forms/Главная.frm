VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Главная 
   Caption         =   "UserForm1"
   ClientHeight    =   3015
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4560
   OleObjectBlob   =   "Главная.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Главная"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit


Private Sub cm_1_Click()
Sheets(1).Activate
Range("A:D").Clear
ActiveSheet.Cells(1, 1) = "ID клиента"
ActiveSheet.Cells(1, 2) = "Фамилия"
ActiveSheet.Cells(1, 3) = "ID машины"
Cells(1, 1).Activate
Сведения.Show
End Sub

Private Sub cm_2_Click()
Sheets(2).Activate
Range("A:D").Clear
ActiveSheet.Cells(1, 1) = "ID машины"
ActiveSheet.Cells(1, 2) = "Цена за час"
Cells(1, 1).Activate
Справочник.Show
End Sub

Private Sub cm_3_Click()
Calculation
End Sub

Private Sub cm_4_Click()
End
End Sub


Private Sub UserForm_Click()

End Sub
