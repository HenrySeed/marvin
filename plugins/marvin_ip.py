import subprocess

def ip():
    proc = subprocess.Popen(['dig +short myip.opendns.com @resolver1.opendns.com'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    try:
        address = str(out.decode("utf-8")).replace('\n', '')
    except:
        address = str(out.decode("utf-8"))

    print('    Your public IP address is ' + address)


commands = [('ip', ip)]
help_options = [('ip', 'Gives you your current ip')]
