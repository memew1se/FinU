Attribute VB_Name = "Practice6"
Option Explicit

Sub Edit()

Dim i As Integer

Load EditForm

i = ActiveCell.Row
EditForm.TextBox1.Text = Worksheets(1).Rows(i).Cells(1).Value
EditForm.TextBox2.Text = Worksheets(1).Rows(i).Cells(2).Value
EditForm.TextBox3.Text = Worksheets(1).Rows(i).Cells(3).Value

EditForm.Show

End Sub

Sub Search()

Load SearchForm
SearchForm.Show

End Sub
