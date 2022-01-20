from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align:center">我的第一个网页</h1>'
    line2 = '<img src="https://z3.ax1x.com/2021/08/25/hV0alT.jpg" width = 950>'
    return HttpResponse(line1 + line2)
