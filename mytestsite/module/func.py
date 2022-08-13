import requests
from datetime import datetime
import time

RobotIP = "192.168.3.165"
RobotPort = "6660"
MacAddress = "0C:54:15:A6:55:EA"
Mac = {"mac": MacAddress}
URL = "http://" + RobotIP + ":" + RobotPort

FMSIP = "172.20.10.4"
FMSPort = "6600"
FMSURL = "http://" + FMSIP + ":" + FMSPort
then = datetime(1970, 1, 1, 0, 0, 0)

def solveRequestFull():
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    return s

def GetDock():
    data = {
        "option" : "all"
    }
    try:
        s = solveRequestFull()
        data = s.post(url = FMSURL + "/get_dock", json = data)
        return data.json()
    except:
        print("let it sleep.")
        time.sleep(5)
        return "let it sleep."

def GetTarget():
    data = {
        "option" : "all"
    }
    try:
        s = solveRequestFull()
        data = s.post(url = FMSURL + "/get_target", json = data)
        return data.json()
    except:
        print("let it sleep.")
        time.sleep(5)
        return None

def GetAGV():
    data = {
        "option" : "all"
    }
    try:
        data = requests.post(url = FMSURL + "/get_agv", json = data)
        return data.json()
    except:
        print("let it sleep.")
        time.sleep(5)
        return "let it sleep."

def MoveToIntersection():
    timedelta = (datetime.now()-then).total_seconds()
    data = {
        "start_time": timedelta,
        "using_time": 300,
        "userid": 15938,
        "robot_type": 0,
        "robot_mode": [1,1,0],
        "task_arr": [
            ["DockTo", ["dock_", "Lab0722@1F"]]
        ]
    }
    try:
        s = solveRequestFull()
        data = s.post(url = FMSURL + "/set_mission", json = data)
        print(data.json())
    except :
        time.sleep(5)

def MoveTo(target):
    target = int(target) - 1
    timedelta = (datetime.now()-then).total_seconds()
    print(timedelta)

    data = {
        "start_time": timedelta,
        "using_time": 300,
        "userid": 15938,
        "robot_type": 0,
        "robot_mode": [1,1,0],
        "task_arr": [
            ["DockTo", ["dock_"+str(target), "Lab0722@1F"]]
        ]
    }
    try:
        s = solveRequestFull()
        data = s.post(url = FMSURL + "/set_mission", json = data)
        print(data.json())
    except :
        time.sleep(5)
    

