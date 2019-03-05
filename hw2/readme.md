# HW2 - Homework for unit 2 - The VBA of wallstreet

## Submissions

### Screenshots

### 2014
![2014](./HW2_RPS_2014_Screenshot.png)

### 2015
![2015](./HW2_RPS_2015_Screenshot.png)

### 2016
![2016](./HW2_RPS_2016_Screenshot.png)

### Separate VBA scripts

### Easy solution
* [Easy Solution](./RPS_HW2_Easy_Solition.vbs)

### Medium solution
* [Medium Solution](./RPS_HW2_Medium_Solition.vbs)

### Hard Solution
* [Hard Solution](./RPS_HW2_Hard_Solition.vbs)

## Notes and Observations

    I treated any stocks that did an initial public offering (IPO) during 
    any years to be an outlier. This is because during the year 2015, when 
    that happened, there were a total of 117 IPOS, but only one was included. 
    [Here is the source of that data.](https://site.warrington.ufl.edu/ritter/files/2016/03/Initial-Public-Offerings-Updated-Statistics-2016-03-08.pdf)

    Additionally, checking each time for just 1 stock would have been a 
    minor performance hit. This stock was treated like an outlier and 
    handled like an error.

    Additionally, there are opportunities to improve the performance of my code. 
    Instead of assigning the ending stock price in each iteration of the loop, 
    I could have just read it when the ticker changed. The code currently 
    functions, however and the performance improvement has been added to technical debt.

