# socks4gui
- a socks4 server based on twisted framework
- graphic UI (Qt4)
- multi platform (Windows/Linux/MacOS)
- log/on-air modify traffic
- user-defined script (python)
> fork from [socks4 by spk] (https://github.com/superkhung/socks4) :ok_hand:
abcd <br>
hihi
## operation
![model] (https://github.com/trichimtrich/socks4gui/blob/master/model.png?raw=true)

## requirement
- Python
- twisted framework
- Qt Libraries
- SIP / PyQt4

## installation
### python / twisted framework
`pip install twisted`

### QtLib / PyQt4
#### Windows
Suitable release for python (2./3.)
![PyQt4] (https://www.riverbankcomputing.com/software/pyqt/download)

#### Linux / MacOS
1. Qt Libraries
##### Linux
`sudo apt-get install python-dev build-essential qt4-dev-tools libqt4-dev libqt4-core libqt4-gui`
##### MacOS
`brew install qt`

2. Download / install SIP
`wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.18.1/sip-4.18.1.tar.gz`
`tar xzvf sip-4.18.1.tar.gz`
`cd sip-4.18.1`
`python configure.py`
`make`
`sudo make install`

3. Download / install PyQt4
