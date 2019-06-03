# socks4gui

forked from [socks4 by spk](https://github.com/superkhung/socks4) 👌, with addtional features:

- a socks v4 server based on twisted reactor framework.
- supports graphic UI (PyQt5).
- supports multi platform (Windows/Linux/MacOS). Thanks to Qt5.
- supports traffic logging and on-air packet filtering.
- user-defined scripting. [Check example](/scripts)

## Traffic flow

- Decap module: user-defined script (decode/decrypt/...)
- Encap module: user-defined script (encode/encrypt/...)
- Replace/Ignore mode: modify packet

![model](https://github.com/trichimtrich/socks4gui/blob/master/docs/img/model.png?raw=true)

*❗module can be disable (redstar)*

*❕transmit packet with no modifying when disable all modules (redline)*

## Dependencies

Only supports for `Python 3`. You can check out the `requirements.txt`
- twisted framework
- PyQt5 Libraries

All platform 
```
pip -i requirements.txt
<or>
pip3 -i requirements.txt
```

## Usage

- Run program `chmod +x socks4gui.py; ./socks4gui.py`

![Screenshot](https://github.com/trichimtrich/socks4gui/blob/master/docs/img/screenshot.png?raw=true)

- All you got to do is hit the `start` button and enjoy your socks server.

## TODO

- Think about data storage
- Filter for cdn/static assets? / large request?
- Separate app into modules
- New form design?
- 

## License

GPL v3