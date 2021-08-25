# VLC Connect

Control VLC with a custom Web UI. Play audio and video from the internet or from local storage.

## Features
- Uses the [VLC](https://pypi.org/project/python-vlc/) python module to utilize VLC features such as playing audio and video
- Uses the [youtube_dl](https://pypi.org/project/youtube_dl/) python module to get URL streams from youtube to play in VLC

*Note: More features will be added in the future such as media playback from other sources*

## Installation

1. Download the zip file of the [repository](https://github.com/alexmbd/vlc-connect/archive/refs/heads/main.zip) or get it with other methods provided by GitHub
2. Extract the zip file
3. Use pip to install the requirements
	```
	pip3 install -r requirements.txt
	```

## Usage
#### For http://localhost:5000 or http://127.0.0.1:5000
1. In the folder containing **app.py**, open a terminal then type `flask run`
2. Open a web browser and enter http://localhost:5000 or http://127.0.0.1:5000
3. It will redirect you to the home page of the application and it is ready to use

*Note: You can only access the site (http://localhost:5000 or http://127.0.0.1:5000) from the same machine. In other words, other devices cannot connect to the specified link. Use the method below to setup a server that any device connected to the same network can access.*

#### For http://LOCAL_IP:PORT
1. In the folder containing **app.py**, open a terminal then type `flask run -h [LOCAL_IP] -p [PORT]`
2. Open a web browser and enter http://LOCAL_IP:PORT
3. It will redirect you to the home page of the application and it is ready to use

*Note (LOCAL_IP): To get your local IP, type in the terminal `ipconfig` (Windows) or `ifconfig` (Linux). Find the IPv4 Address, typically starting with 10.x.x.x, 172.x.x.x or 192.x.x.x ([see more about private IPv4 addresses](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_addresses))*

*Note (PORT): For the port number, flask defaults to 5000 but you can change it to whatever you like. However, there are reserved port numbers so be mindful of that specific numbers ([see more about ports](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers))*

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
