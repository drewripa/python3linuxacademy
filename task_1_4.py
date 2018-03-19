import argparse
import subprocess

parser = argparse.ArgumentParser(description='Process killer aka Hitmen')
parser.add_argument('port_number', type=int, help='Port number for assassination')

args = parser.parse_args()

#I'm using CentOS7 + httpd instead of Python simplehttpserver
port = 'http' if args.port_number == 80 else args.port_number

text = (subprocess.run(["sudo","lsof", "-n", f"-i6TCP:{port}"], stdout=subprocess.PIPE)).stdout.decode()
for line in text.splitlines():
    line_args = line.split()
    if line_args[2] == 'root':
        print(f"Killing {line_args[1]} PID")
        subprocess.run(["sudo", "kill", f"{line_args[1]}"])
        break

