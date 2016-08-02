# socks4gui
> forked from [socks4 by spk] (https://github.com/superkhung/socks4) :ok_hand:

- a socks4 server based on twisted framework
- graphic UI (Qt4)
- multi platform (Windows/Linux/MacOS)
- log/on-air modify traffic
- user-defined script (python)

## Operation
![model] (https://github.com/trichimtrich/socks4gui/blob/master/model.png?raw=true)

## Requirement
- Python
- twisted framework
- Qt Libraries
- SIP / PyQt4

## Installation

### python / twisted framework
All platform `pip install twisted`

### QtLib / PyQt4

#### Windows
Suitable release for python (2./3.)
[PyQt4] (https://www.riverbankcomputing.com/software/pyqt/download)

#### Linux / MacOS
- Qt Libraries

##### Linux
`sudo apt-get install python-dev build-essential qt4-dev-tools libqt4-dev libqt4-core libqt4-gui`

##### MacOS
`brew install qt`

- SIP

```
wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.18.1/sip-4.18.1.tar.gz
tar xzvf sip-4.18.1.tar.gz
cd sip-4.18.1
python configure.py
make
sudo make install
```

- PyQt4

Download source code (Linux) [https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt-x11-gpl-4.11.4.tar.gz/download] / (MacOS) [https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt-mac-gpl-4.11.4.tar.gz/download]

```
cd <extracted folder>
python configure.py
make
sudo make install
```
