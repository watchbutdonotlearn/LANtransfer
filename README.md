# LANtransfer
## Overview



A project for transferring files on LAN.


This project consists of two parts: one is a c++ program that is actually just a wrapper over netcat, but the command is a hundred times easier to type and remember. Thus, to run it, you'll need to have netcat installed. The other program is a set of two python scripts that are modified versions of the code found at my other project, a python shared clipboard, which can be found [here](https://github.com/watchbutdonotlearn/PySharedclipboard).


## The C++ program


To send a file, use the command `./program send file.txt [ip]`.


To receive a file, use the command `./program receive`.


## The Python scripts


Unlike the [program](https://github.com/watchbutdonotlearn/PySharedclipboard) it is based on, these two scripts which only deal with file transfer requires no third party libraries to run. Run `python server.py` and `python client.py` in two seperate terminal windows to get the program started.  


Next, after running the client script, you will be prompted for the IP address of the computer you want to connect to. Keep in mind that this is the local IP address of the target computer, and that the scripts must be run between two computers on LAN. Dialing in the IP of a remote computer on another network will not work.


Once that is done, everything is set up. Type the name of the file which you want to send into the client script (note that the file must be in the same directory as the script) and press enter, and the file will be sent to the receiving computer. A file will be created called received_file in the directory the server script is in. 
