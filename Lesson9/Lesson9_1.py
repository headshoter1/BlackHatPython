import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()  # default .ssh/known_hosts ssh.load_host_keys("~/.ssh/known_hosts) - custom

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="10.10.10.131", username="kali", password="kali")
stdin, stdout, stderr = ssh.exec_command("ls -la")

print(stdin)
print(stdout.read().decode("UTF-8"))
print(stderr.read())
sftp_client = ssh.open_sftp()
sftp_client.get("/home/kali/secret.txt", "./secret666.txt")

ssh.get_transport()
ssh.close()