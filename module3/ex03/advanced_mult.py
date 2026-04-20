#!/usr/bin/env python3

i = 0 
# j = 0

while (i <= 10):
	j = 0
	print(f"Table of {i}:", end = " ")
	while(j <= 10):
		print(i * j, end = " ")
		j += 1
	print()
	i += 1
