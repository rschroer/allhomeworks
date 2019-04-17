Sub EasySolution()
Dim i As Double
Dim j As Double
Dim Ticker As String
Dim sht As Worksheet
Dim Lastrow As Double
Dim stockvolume As Double


For Each sht In Worksheets
    'Initial Variable setting
    i = 1

'Find the last row in the spreadsheet
    Lastrow = sht.Cells(sht.Rows.Count, "A").End(xlUp).Row

'This outerloop just goes through the rows.
    For j = 2 To Lastrow
'Check to see if the ticker symbol is the same as last row
        Ticker = sht.Cells(j, 1).Value
            If Ticker = sht.Cells(j - 1, 1).Value Then
'if the stock is the same, then it adds the volume to the sum
               stockvolume = stockvolume + sht.Cells(j, 7).Value
               sht.Cells(i, 10).Value = stockvolume
'if the ticker is different, then it and resets the volume to cell and writes that initial volume and ticker to the summary
            Else
                i = i + 1
                sht.Cells(i, 9).Value = Ticker
                stockvolume = sht.Cells(j, 7).Value
                sht.Cells(i, 10).Value = stockvolume
            End If
    Next j
    

'Create the headers for the column
    sht.Range("I1").Value = "Ticker"
    sht.Range("J1").Value = "Total Volume"
    
Next sht

End Sub
