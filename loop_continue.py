#!/bin/env python3

count = 1
while count <= 20:
   if count % 2 == 0:
         #count += 1
         continue
   
   print(f"We are couting odd numbers: {count}")
   count += 1