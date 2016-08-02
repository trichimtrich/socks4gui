# socks4gui
> forked from [socks4 by spk] (https://github.com/superkhung/socks4) :ok_hand: :ok_hand: :ok_hand:

- a socks4 server based on twisted framework
- graphic UI (Qt4)
- multi platform (Windows/Linux/MacOS)
- log/on-air modify traffic
- user-defined script ([python example] (https://github.com/trichimtrich/socks4gui/blob/master/testscript.py))

## Operation
- Decap module: user-defined script (decode/decrypt/...)
- Encap module: user-defined script (encode/encrypt/...)
- Replace/Ignore mode: modify packet

![model] (https://github.com/trichimtrich/socks4gui/blob/master/model.png?raw=true)

*:exclamation: module can be disable (redstar)*
*:grey_exclamation: transmit packet with no modifying when disable all modules (redline)*

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
Suitable release for python (2/3) at [PyQt4 Homepage] (https://www.riverbankcomputing.com/software/pyqt/download)

#### Linux / MacOS
- Qt Libraries

**Linux:** `sudo apt-get install python-dev build-essential qt4-dev-tools libqt4-dev libqt4-core libqt4-gui`

**MacOS:** `brew install qt`

- [SIP] (https://www.riverbankcomputing.com/software/sip/download)
```
wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.18.1/sip-4.18.1.tar.gz
tar xzvf sip-4.18.1.tar.gz
cd sip-4.18.1
python configure.py
make
sudo make install
```

- [PyQt4] (https://www.riverbankcomputing.com/software/pyqt/download)

Download source code [Linux] (https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt-x11-gpl-4.11.4.tar.gz/download) / [MacOS] (https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt-mac-gpl-4.11.4.tar.gz/download)
```
cd <extracted folder>
python configure.py
make
sudo make install
```

## Usage

`python socks4gui.py`

![Screenshot] (https://github.com/trichimtrich/socks4gui/blob/master/screenshot.png?raw=true)
Almost like [burp suite] (https://portswigger.net/burp/) :heart_eyes: :heart_eyes: :heart_eyes:

Hehe. Enjoy :smiley:
