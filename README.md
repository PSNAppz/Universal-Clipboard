# Universal Clipboard
Universal clipboard is useful when you want to copy something(preferrably plaintext) from one device to another. It works for any OS. Currently it only supports plaintext. 

-----
### Curated Features

- [x] Copy plaintext from one device to another
- [ ] Copy images/files from one device to another
- [ ] Work outside localnetwork

----
## Installation & Usage 

### Setup the virtual environment
``Python version: 3.10 is recommended. ``

``` bash
virtualenv venv --python=python3.10
```
Source the virtual environment:
``` bash
source venv/bin/activate
```
Install the dependencies
``` bash
pip install -r requirements.txt
```

### Run the server 
``` bash
python server.py
```
### Update the ip address of the server

Update the below line inside the `universal_clipboard.py` file: 
``` python
sio.connect('ws://<server_ip>:5007')  # Update the ip address of the server
```

### Run the client
``` bash
python universal_clipboard.py
```
----
## Contributing
All contributions are welcome. See the curated list above for ideas. If you have an idea, please open an issue or pull request.