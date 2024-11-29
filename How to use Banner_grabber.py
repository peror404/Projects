usage: banner_grabber.py -t TARGET [-s SPECIFIC] [-r RANGE] [-o OUTPUT FILE]

TARGET can be any website or IP Address
Options: 
-s : by this option you can insert specific port number to scan.
example : banner_grabber.py -t TARGET -s 80      //here port no. 80 is specific port.
-r : this option is for declarying rang of port numbers.
example : banner_grabber.py -t TARGET -r 1-100   //here it will scan all the port no. between 1 to 100 .
-o : this option used for redirecting the output to any file .
example : banner_grabber.py -t TARGET -s 80 -o Output_file.txt   // it will store all the output in Output_file.txt file.

[-h] : this option is for help.
