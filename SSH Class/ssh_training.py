# pylint: disable=no-name-in-module
# pylint: disable=function-redefined
# pylint: disable=import-error

import paramiko as paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", "port", "username","password")


#Run bash commands remotely:
stdin, stdout, stderr = ssh.exec_command("Command goes here")
#input, output, errors
print(stdout.readlines())

stdin, stdout, stderr = ssh.exec_command("touch demofile")
stdin, stdout, stderr = ssh.exec_command("cat demofile")
print(stdout.readlines())


#Upload a file:
sftp = ssh.open_sftp()

dest_path = "/usr/script.py"
og_path = "SDET Training Course/SSH Class/script.py"

sftp.put(og_path, dest_path)


#Download a file:
sftp = ssh.open_sftp()

dest_path = "SDET Training Course/SSH Class/script.py"
og_path = "/usr/script.py"

sftp.get(og_path, dest_path)


#Run scripts:
stdin, stdout, stderr = ssh.exec_command("python script.py OR ./script.py") #depends if the file has a shebang or not.


#Close the connection:
ssh.close()