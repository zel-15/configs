import subprocess
proc = subprocess.check_output(['nmcli device wifi'], shell=True,)
proc = proc.decode("utf-8")
print(proc)
while True:
    ssid = input('Enter SSID:')
    password = input('Enter Password:')
    checkerr = subprocess.Popen(['nmcli', 'device', 'wifi', 'connect', ssid], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    checkerr.wait()
    (stdout, stderr) = checkerr.communicate()
    if checkerr.returncode != 0:
        print(stderr)
        continue
    else: 
        print("sucess")
        break
