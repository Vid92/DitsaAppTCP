import paramiko
from scp import SCPClient

import appsettings
from appsettings import useHostname

class FilesServer():
	def __init__(self):
	#def openFl(self):
		try:
			ssh_client = paramiko.SSHClient()
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			#ssh_client.connect(hostname='rpitablet.local', username='pi', password='paulina84')
			#ssh_client.connect(hostname=useHostname, username='CEX', password='rom25123012')
			ssh_client.connect(hostname='ditsa-Lenovo-C20-00.local', username='ditsa', password='ditsanet')

			'''
			sftp = ssh_client.open_sftp()
			# This will remove a file
			sftp.remove("/home/pi/Documents/New.txt")
			# This will remove a folder
			sftp.rmdir("/home/pi/Documents/New")
			sftp.close()
			'''

			# SCPCLient takes a paramiko transport as an argument
			scp = SCPClient(ssh_client.get_transport())

			# This will copy a file
			#scp.get(remote_path='/home/ditsa/TestLogs/4-SGL.txt', local_path='')
			# This will copy a whole directory
			#scp.get(remote_path='/home/ditsa/DitsaNet/FormationDataFiles/', local_path='/Users/cex/Desktop/LayoutEditor/', recursive=True)
			scp.get(remote_path='/home/ditsa/DitsaNet/ProfileEditorPrograms/', local_path='/home/pi/DitsaNetServer/', recursive=True)
			#scp.get(remote_path='/Users/cex/TestLogs/', local_path='', recursive=True)

			scp.close()
			ssh_client.close()
			print("successful")
		except Exception as e:
			print("Error : " + str(e))


if __name__ == '__main__':
	print("FilesServer")

	fl = FilesServer()