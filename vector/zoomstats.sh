#!/bin/sh

set -e

[ ! -z "$1" ] || exit 1

FILE=$(mktemp --tmpdir "$(basename $0).XXXXX") || exit 1
trap "rm -f $FILE" EXIT

find cache/bolder/$1 -type f -print0 | du -b --apparent-size --files0-from=- | cut -f -1 | sort -n > $FILE

N=$(wc -l $FILE | awk '{print $1}')

AVG=$(awk '{ total += $1; count++ } END { print total/count }' $FILE)
P50=$(dc -e "$N 2 / p")
P75=$(dc -e "$N 75 * 100 / p")
P95=$(dc -e "$N 99 * 100 / p")
P99=$(dc -e "$N 99 * 100 / p")

echo "$1"
echo "$AVG"
awk "FNR==$P50 || FNR==$P75 || FNR==$P95 || FNR==$P99" $FILE

