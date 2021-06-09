import paramiko
from scp import SCPClient

import appsettings
from appsettings import useHostname


class FilesReport():
	def __init__(self,pssw):
	#def openFl(self):
		self.pssw = pssw
		#esta parte de pssw que de los datos ditsaserver
		for i in range(len(useHostname)):
			try:
				ssh_client = paramiko.SSHClient()
				ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				#ssh_client.connect(hostname='rpitablet.local', username='pi', password='paulina84')
				#ssh_client.connect(hostname=useHostname, username='CEX', password='rom25123012')
				ssh_client.connect(hostname=useHostname[i], username='pi', password=self.pssw[i])

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
				scp.get(remote_path='/home/pi/DitsaNetServer/FormationDataFiles', local_path='/home/ditsa/DitsaNet/', recursive=True)
				#scp.get(remote_path='/Users/cex/TestLogs/', local_path='', recursive=True)

				scp.close()
				ssh_client.close()
				#print("successful")
			except Exception as e:
				print("Error : " + str(e))


if __name__ == '__main__':
	print("FileReports")

	fl = FilesReport()
