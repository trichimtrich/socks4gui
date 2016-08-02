# socks4gui
a multi-platform socks4 server based on twisted framework with graphic UI, log/on-air modify traffic, user-defined script (python)

## model / operation

## requirement
Python
Qt Libraries
PyQt4
twisted framework for python

## installation
### python / twisted framework
`pip install twisted`

### QtLib / PyQt4
#### Windows
Suitable release for python (2./3.)
https://www.riverbankcomputing.com/software/pyqt/download

#### Linux / MacOS
1. Qt Libraries
`sudo apt-get install python-dev build-essential qt4-dev-tools libqt4-dev libqt4-core libqt4-gui`
2. Download / install SIP
`wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.18.1/sip-4.18.1.tar.gz
tar xzvf sip-4.18.1.tar.gz
cd sip-4.18.1
python configure.py
make
sudo make install`
3. Download / install PyQt4
