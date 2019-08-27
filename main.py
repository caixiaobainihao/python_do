#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'cloudtogo'

from flask import render_template
from flask import Flask
import os
import redis
import ctypes
import sys
app = Flask(__name__)

reload(sys)
sys.setdefaultencoding('utf8')


################################################################################

# 请修正下面错误的"Hello, word"的拼写！
# 请在修改完成后，通过主菜单 Git代码库/提交 ... 菜单项完成代码的Commit 和 Push。
# Push完成后回到 “趣码—应用工厂” 中该项目的 “蓝图” 页面( http://factory.cloudtogo.cn/project/blueprint?id=last )，点击发布新实例后，即可看到修改后的效果。

## 错误在这里 ___
#              |
#              V
msg = 'Hello, world! i love you'

################################################################################


@app.route('/')
def hello():
    
    envURL = os.environ.get("WEBIDE")
    envRedis = os.environ.get("REDIS")

    r = redis.StrictRedis(host=str(envRedis), port=6379)
    hits = r.get('hits')
    if hits:
        hits = r.get('hits').decode('utf-8')
    else:
    	hits = '0'
    hits = str(int(hits) + 1)
    r.set('hits', hits)

    btnContent = '修改我的代码'
    body = '恭喜您成功发布了Python项目... 啊！word 拼写错误，尝试修改代码解决这个问题吧。'

    if msg != 'Hello, word!':
        btnContent = '搭建我的袜子电商网站'
        body = '恭喜您成功修复了代码！您可以通过创建一个袜子电商网站来体验行云趣码一站式开发平台更浩瀚的功能。'
        envURL = 'http://help.cloudtogo.cn/tutorial/55b67d34-141d-11e7-93ae-92361f002671.html'

    return render_template('hello.html', Hits=hits, Body=body, WebIDE=envURL, Msg=msg, ButtonContent=btnContent)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

