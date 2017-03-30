'''
콘솔에서 파라매터로 프로젝트의 네임만 입력하면 현재 디렉토리 기준으로 프로젝트 구조 생성해줌
'''
import os 
import sys

def make_folder(proj_name):
    os.mkdir("./{}".format(proj_name))
    os.mkdir("./{}/{}".format(proj_name,proj_name))
    os.mkdir("./{}/{}/static".format(proj_name,proj_name))
    os.mkdir("./{}/{}/templates".format(proj_name,proj_name))

def make_init_files(proj_name):
    tmp ="from {} import app\nif __name__ == '__main__':\n\tapp.run(host='0.0.0.0')"
    tmp2 = "from flask import Flask\n\napp = Flask(__name__)\n\n\n@app.route('/')\ndef {}():\n\treturn 'hello world'"

    f = open("./{}/app_start.py".format(proj_name),"w")
    f.write(tmp.format(proj_name))
    f.close()

    f = open("./{}/{}/__init__.py".format(proj_name,proj_name),"w")
    f.write(tmp2.format(proj_name))
    f.close()


def make_files():
    if len(sys.argv) != 1:
        proj_name = sys.argv[1]
        make_folder(proj_name)
        make_init_files(proj_name)   
    else:
        print("ex)python createProj.py 'Your Project name'") 


if __name__ == "__main__":
    make_files()









