#!/usr/bin/env bash

ARQUIVO=$1

awk 'NR > 3 { OFS="\t"; print $5,$6,$7,$9,$11 }' $ARQUIVO | grep -vi -E 'low_complexity|simple_repeat|trna|rrna|unknown|satellite|snrna'
