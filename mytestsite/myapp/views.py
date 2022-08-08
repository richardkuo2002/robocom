from django.shortcuts import render
from module import func, LucasKanade

# Create your views here.

MainTarget = ""
CrossIntersection = False


def test(request):
    # output = str(func.GetDock())
    # func.MoveTo(1)
    # output += str(func.GetAGV()["value"]["agv"][0][6])
    return render(request, "page.html", locals()) 

def move(request, target):
    global MainTarget
    AGVStatus = func.GetAGV()["value"]["agv"][0][6]

    # if MainTarget != target:
    #     MainTarget = target
    # global CrossIntersection
    # if int(target) < 30 and CrossIntersection == False:
    #     if AGVStatus == "standby":
    #         MoveToIntersection()
    #         return render(request, "move.html", locals())
    #     if AGVStatus == "end":
    #         while(1):
    #             if LucasKanade.OpticalFlow():
    #                 CrossIntersection = True
    #                 func.MoveTo(target)
    #                 break

    if AGVStatus == "standby":
        func.MoveTo(target)
        print(target)
        return render(request, "move.html", locals())
    elif AGVStatus == "running":
        print(target)
        return render(request, "move.html", locals())
    elif AGVStatus == "end":
        MainTarget = ""
        return render(request, "return.html", locals())
    else :
        return render(request, "report.html", locals())

def choose(request):
    return render(request, "choose.html", locals())

def report(request):
    return render(request, "report.html", locals())


