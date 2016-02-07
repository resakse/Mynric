# Mynric
Python library to get information from Malaysian NRIC (MyKad).

Usage:

```python
from myic import myic

ic = myic('791113-11-1111')
ic.age()
'36 years 2 month and 25 days'
ic.gender()
'Male'
ic.birthday()
'13 Nov 1979'
ic.upcoming()
'in 9 month and 5 days'
```
add option 'm' or 'malay' for result in Malay.
```python
ic = myic('790208-11-1111','m')
ic.age()
'36 tahun 11 bulan dan 30 hari'
ic.gender()
'Lelaki'
ic.upcoming()
'dalam masa 5 jam lagi'
ic.birthday()
'08 Feb 1979'
```

#ToDo: 
1. Fetch country code from JPN website
