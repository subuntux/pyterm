#!/bin/bash
cd $HOME
echo ""
echo "[*] Start Setup"
echo ""
mv rish* $HOME/.cache/adb/
cp /data/data/com.termux/usr/shared/pyterm/adb $PREFIX/bin/
chmod +x $PREFIX/bin/*
echo ""
echo "[*] Finish run: adb shell"
echo ""

