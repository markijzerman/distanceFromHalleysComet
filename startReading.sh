#!/bin/bash
rm my.log
wolfram -script distancetohalley.wl 2>&1 | tee my.log &
python halleyToLCD.py

