from subprocess import Popen
from subprocess import PIPE

popen = Popen("top -l 1 | grep bird", shell=True, stdout=PIPE)
out, error = popen.communicate()
print(out)