# IPlistGenerator


Description:
A simple IPv4 list generator written in python. This will take your CIDR notation (example 192.168.X.X/32) and expand it into a readable list of all IPs within that notation.

Usage:
To expand one single CIDR notation-
  ipListGen 192.168.X.X/27

To save to an output file-
  ipListGen 192.168.X.X/27 -o output.txt

To use an input file for multiple notations and output the results-
  ipListGen -i input.txt -o output.txt
  (The input file must have only one notation per line)

