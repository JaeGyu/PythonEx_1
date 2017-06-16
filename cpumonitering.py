from subprocess import Popen
from subprocess import PIPE
from time import sleep
import sys

"""
osX 라서 top -l 1 을 헤 준다.
linux의 top -n 1 과 같은 효과 이다.
top을 한번만 실행하고 프로세스를 종료 해준다
"""
cmd_filter = ""

def exec_bash(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    (ret, err) = p.communicate()
    return ret.strip()

def get_info():
    cmd = "info"
    if cmd_filter != "":
        cmd = "top -l 1 | grep '%s'" % cmd_filter
        print(cmd)
        ret = exec_bash(cmd)
        print(ret)

def get_monitoring_input():
    global cmd_filter  #글로벌 변수 적용안하도록 리팩토링 할 것
    print("현재 동작 중인 프로세스를 표시하기 위해 필터 조건을 입력하세요")
    cmd_filter = input("입력하지 않으면 모든 프로세스를 출력합니다. : ")
    info_list = get_info()

if __name__ == "__main__":
    mon_info_list = get_monitoring_input()
