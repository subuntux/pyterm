# pyterm
Pyterm is an Termux Tool you can download the .deb from the releases or you can build the packahe on your system

Own Build:

```bash
pkg update -y
pkg install python3 termux-create-package git -y
git clone https://github.com/subuntux/pyterm
cd pyterm
termux-create-package *.json
dpkg -i *.deb
```
