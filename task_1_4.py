import argparse
import subprocess

parser = argparse.ArgumentParser(description='Process killer aka Hitmen')
parser.add_argument('port_number', help='Port number for assassination')

args = parser.parse_args()

#I'm using CentOS7 + httpd instead of Python simplehttpserver
port = 'http' if args.port_number == 80 else args.port_number

print(subprocess.run(["lsof", "-n", f"-i6TCP:{port}"]))

