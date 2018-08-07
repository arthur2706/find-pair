# find-pair
small program to find 2/3 gifts specifying a budget.

takes as an input a file name and a budget and tries to find max possible gifts according to budget. 

the file should be a comma delimited set of rows of gift name and its price.



try:

```console
$ ./find-pair ./tests/prices.txt 2500
Candy Bar 500, Earmuffs 2000

$ ./find-pair ./tests/prices.txt 2300
Paperback Book 700, Headphones 1400

$ ./find-pair ./tests/prices.txt 10000
Earmuffs 2000, Bluetooth Stereo 6000

$ ./find-pair ./tests/prices.txt 1100
Not possible

$ ./find-trio ./tests/prices.txt 10000
Headphones 1400, Earmuffs 2000, Bluetooth Stereo 6000

$ ./find-trio ./tests/prices.txt 1000
Not possible
```
