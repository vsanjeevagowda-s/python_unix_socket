# import subprocess

# def run_command(command):
#     p = subprocess.Popen(command,
#                          stdout=subprocess.PIPE,
#                          stderr=subprocess.STDOUT)
#     return iter(p.stdout.readline, b'')

# command = 'ls -al'.split()
# for line in run_command(command):
#     print(line)

# ===================

from subprocess import check_output
from shlex import split

res = check_output(split('ls -lah'))
print(res)

# ===================
# import subprocess

# def sh(cmd, input=""):
#     rst = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input.encode("utf-8"))
#     assert rst.returncode == 0, rst.stderr.decode("utf-8")
#     return rst.stdout.decode("utf-8")

# print(sh("ls -lah"))