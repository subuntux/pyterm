#!/bin/bash
cd $HOME
echo ""
echo "[*] Start Download"
echo ""
wget https://github.com/subuntux/pyterm/releases/download/v.1.0/shizuku.tar.xz
tar -xJf shizuku.tar.xz
mv rish* .cache/adb
cp /data/data/com.termux/files/usr/shared/pyterm/adb $PREFIX/bin/
chmod +x $PREFIX/bin/*
echo ""
echo "[*] Finish"
echo "[*] Run: adb shell"
echo ""
