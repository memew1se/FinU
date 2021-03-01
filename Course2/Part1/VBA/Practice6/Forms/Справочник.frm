VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Справочник 
   Caption         =   "UserForm3"
   ClientHeight    =   3015
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4560
   OleObjectBlob   =   "Справочник.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Справочник"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cm_OK_Click()
Dim i As Integer
Sheets(2).Activate
ActiveCell.Offset(1, 0).Activate
i = ActiveCell.Row
ActiveSheet.Cells(i, 1) = TextBox_carID
ActiveSheet.Cells(i, 2) = TextBox_rent
i = ActiveCell.Row + 1
End Sub

Private Sub cm_exit_Click()
Hide
End Sub

