'Medium solution
Sub MediumSolution()
Dim i As Double
Dim j As Double
Dim Ticker As String
Dim sht As Worksheet
Dim Lastrow As Double
Dim stockvolume As Double
Dim StartingPrice As Double
Dim EndingPrice As Double

For Each sht In Worksheets
    'Initial Variable setting
    i = 1

'Find the last row in the spreadsheet
    Lastrow = sht.Cells(sht.Rows.Count, "A").End(xlUp).Row

'This outerloop just goes through the rows and assigns the Ticker variable of that row.
    For j = 2 To Lastrow + 1
        Ticker = sht.Cells(j, 1).Value
'if the stock is the same as the previous, then it adds the volume to the sum
'and changes the ending price
            If Ticker = sht.Cells(j - 1, 1).Value Then
               stockvolume = stockvolume + sht.Cells(j, 7).Value
               EndingPrice = sht.Cells(j, 6)
               
 'This line of code would be used to calculate starting price if there was an Initial Public Offering (IPO)
 'during the year. It is not included for performance reasons as I believe the inclusion of the 1 IOP is an outlier.
               'If StartingPrice = 0 Then
                    'StartingPrice = sht.Cells(j, 3).Value
                'End If


'if the ticker is different, then it writes the volume
'it also calculates the price
            Else
                sht.Cells(i, 12).Value = stockvolume
                sht.Cells(i, 10).Value = EndingPrice - StartingPrice
'This is to avoid divide by 0 error when stocks were new that year. This was a design decision to exclude
'new stocks as there was only one so, it looked like an outlier. Additionally, the questions of
' Which stocks did best or worst in the year?' and 'which ipo's were under/overpriced?' are fundamentally
'different.  According to https://site.warrington.ufl.edu/ritter/files/2016/03/Initial-Public-Offerings-Updated-Statistics-2016-03-08.pdf,
' there were 117 IPOS in 2015. I belive the inclusion of PLNT was a mistake and handled it as an error.
'this choice saved both computing power and programming time.
                If (StartingPrice) = 0 Then
                    sht.Cells(i, 11).Value = "New Stock"
'Calculate the percentage change and format that number
                Else
                    sht.Cells(i, 11).Value = (EndingPrice - StartingPrice) / StartingPrice
                    sht.Cells(i, 11).NumberFormat = "0.00%"
                End If
'Conditional Formatting for the price differential
                If (EndingPrice - StartingPrice) >= 0 Then
                    sht.Cells(i, 10).Interior.ColorIndex = 4
                Else
                    sht.Cells(i, 10).Interior.ColorIndex = 3
                End If
'Set the starting price to the new beginning price and also
'set the stock volume and ticker to the new beginning
                StartingPrice = sht.Cells(j, 3).Value
                i = i + 1
                sht.Cells(i, 9).Value = Ticker
                stockvolume = sht.Cells(j, 7)
            End If
    Next j
    

'Create the headers for the column and change color back to normal
' I considered checking to see if it was the first row for the loop, but I didn't want to
'add that logic to each part of the main loop when I could just correct
'the headers after the fact
    sht.Range("I1").Value = "Ticker"
    sht.Range("j1").Value = "Yearly Change"
    sht.Range("j1").Interior.ColorIndex = 2
    sht.Range("k1").Value = "Percent Change"
    sht.Range("l1").Value = "Total Volume"
    
Next sht
   

End Sub

