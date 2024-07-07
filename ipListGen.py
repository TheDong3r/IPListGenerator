#!/usr/bin/env python3

import ipaddress
import argparse

def print_ipv4_addresses_from_cidr(cidr: str, output_file=None):
 # prints the IPv4 addresses in the CIDR request and writes the expanded lists to an output file, if called via command.  

    try:
        # This Parses the CIDR block
        net_ipv4_address = ipaddress.ip_network(cidr)
        output_lines = [f"Here are the IPv4 addresses from the given CIDR address ({cidr}):\n"]
        
        # Collect each IP address in the network
        for index, ip in enumerate(net_ipv4_address, start=1):
            line = f"{index}: {ip}\n"
            output_lines.append(line)
        
        # Print results or errors to console
        for line in output_lines:
            print(line, end='')
            if output_file:
                output_file.write(line)
    except ValueError as e:
        error_message = f"Error with CIDR {cidr}: {e}\n"
        print(error_message)
        if output_file:
            output_file.write(error_message)

def process_input_file(input_file, output_file):
# Parsing the input file and generating an output file with the expanded IP lists. 

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cidr = line.strip()
            if cidr:
                print_ipv4_addresses_from_cidr(cidr, output_file=outfile)

def main():
 # Parsing command line args.

    parser = argparse.ArgumentParser(description='Generate a list of IP addresses from given CIDR blocks.')
    parser.add_argument('cidr', type=str, nargs='?', help='CIDR block to generate IP addresses from, e.g., 123.45.66.64/27')
    parser.add_argument('-i', '--input', type=str, help='Path to the input file containing CIDR blocks.')
    parser.add_argument('-o', '--output', type=str, help='Path to the output file to save the IP addresses.')

    args = parser.parse_args()

    if args.input and args.output:
        # Process input file and write to output file
        process_input_file(args.input, args.output)
    elif args.cidr:
        # Process a single CIDR block
        if args.output:
            with open(args.output, 'w') as outfile:
                print_ipv4_addresses_from_cidr(args.cidr, output_file=outfile)
        else:
            print_ipv4_addresses_from_cidr(args.cidr)
    else:
        print("Error: You must provide a CIDR block or an input file. Use -h for help.")

if __name__ == "__main__":
    main()

