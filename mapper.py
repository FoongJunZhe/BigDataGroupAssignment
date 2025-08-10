#!/usr/bin/env python3
import sys, re
PATTERN = re.compile(r'^(?P<ip>\S+)')
for line in sys.stdin:
    m = PATTERN.match(line)
    if m:
        print(f"{m.group('ip')}\t1")

