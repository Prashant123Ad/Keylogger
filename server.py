import socket

def server_start():
	host = '0.0.0.0'
	port = 4444

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(1)
	print(f"Listening on {host}:{port}")

	conn, addr = s.accept()
	print(f'Connection from {addr}' )

	try:
		while True:
			data = conn.recv(1024)
			if not data: break
			print(data.decode(), end='')

	finally:
		conn.close()

if __name__ == "__main__":
	server_start()



