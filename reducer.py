#!/usr/bin/env python3
import sys
cur_ip, cur_total = None, 0
for line in sys.stdin:
    ip, n = line.rstrip().split('\t')
    n = int(n)
    if ip == cur_ip:
        cur_total += n
    else:
        if cur_ip is not None:
            print(f"{cur_ip}\t{cur_total}")
        cur_ip, cur_total = ip, n
if cur_ip:
    print(f"{cur_ip}\t{cur_total}")
