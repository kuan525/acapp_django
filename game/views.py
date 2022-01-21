from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align:center">我的第一个网页</h1>'
    line3 = '<hr>'
    line2 = '<img src="https://z3.ax1x.com/2021/08/25/hV0alT.jpg" width = 950>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(reuqest):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<hr>'
    line3 = '<a href="https://imgtu.com/i/I8jV74"><img src="https://z3.ax1x.com/2021/11/08/I8jV74.png" alt="I8jV74.png" border="0" width="2000"/></a>'
    line4 = '<a href="/">返回主页面</a>'
    return HttpResponse(line1 + line4 + line2 + line3)
