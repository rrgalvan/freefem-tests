#!/bin/sh
grep -E "max.+Positivity.+" *.out -m 1 -B2 -A1 --color
