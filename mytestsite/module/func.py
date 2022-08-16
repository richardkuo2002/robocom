import requests
from datetime import datetime
import time

RobotIP = "192.168.3.165"
RobotPort = "6660"
MacAddress = "0C:54:15:A6:55:EA"
Mac = {"mac": MacAddress}
URL = "http://" + RobotIP + ":" + RobotPort

FMSIP = "192.168.0.100"
FMSPort = "6600"
FMSURL = "http://" + FMSIP + ":" + FMSPort
then = datetime(1970, 1, 1, 8, 0, 0)
RobotName = "msi_yellow"
BasicData = {
        "start_time": ((datetime.now()-then).total_seconds()),
        "using_time": 300,
        "userid": 15938,
        "robot_type": 0,
        "robot_mode": [0,0,0],
        "robot_name": RobotName,
        }
MapName = ""

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
    BasicData["task_arr"] = [
            ["DockTo", ["dock_", "Lab0722@1F"]]
        ]
    try:
        s = solveRequestFull()
        data = s.post(url = FMSURL + "/set_mission", json = BasicData)
        print(data.json())
    except :
        time.sleep(5)

def MoveTo(target):
    target = int(target) - 1
    timedelta = (datetime.now()-then).total_seconds()
    print(timedelta)

    BasicData["task_arr"] = [
            ["MoveTo", ["target_" + str(target), "Lab0722@1F"]]
        ]
    try:
        s = solveRequestFull()
        data = s.post(url = FMSURL + "/set_mission", json = BasicData)
        print(data.json())
    except :
        time.sleep(5)
    
def ButtonWait():
    timedelta = (datetime.now()-then).total_seconds()
    print(datetime.now())
    BasicData["task_arr"] = [
            ["ButtonWait", 0, 20],
        ]
    data = requests.post(url = FMSURL + "/set_mission", json = BasicData)
    print(data.json())

def FollowPath(target):
    target = int(target) - 1
    BasicData["task_arr"] = [
            ["FollowPath" + str(target), ["rail_No." + str(target), 0, 700, MapName] ]
        ]
    data = requests.post(url = FMSURL + "/set_mission", json = BasicData)
    print(data.json())

def PauseMission(target):
    Data = {
        "robot_name": RobotName,
        "userid": 15938,
    }
    data = requests.post(url = FMSURL + "/pause_mission_by_robot", json = Data)
    print(data.json())

def ResumeMission(target):
    Data = {
        "robot_name": RobotName,
        "userid": 15938,
    }
    data = requests.post(url = FMSURL + "/resume_mission_by_robot", json = Data)
    print(data.json())

def CancelMission(target):
    Data = {
        "category":"all",
        "task_id": -1
    }
    data = requests.post(url = FMSURL + "/get_mission", json = Data)
    Data = {
        "taskindex": data.json()["value"]["unfinish"][0][0],
        "userid": 15938,
    }
    data = requests.post(url = FMSURL + "/cancel_mission", json = Data)
    print(data.json())
