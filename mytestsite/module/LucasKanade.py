import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time




def OpticalFlow(url, sec):

    
    cap = cv2.VideoCapture(url)

    # 設定 ShiTomasi 角點檢測的引數
    feature_params = dict( maxCorners=100,
                        qualityLevel=0.3,
                        minDistance=7,
                        blockSize=7 )

    # 設定 lucas kanade 光流場的引數
    # maxLevel 為使用影象金字塔的層數
    lk_params = dict( winSize=(15,15),
                    maxLevel=2,
                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # 產生隨機的顏色值
    color = np.random.randint(0,255,(100,3))

    # 獲取第一幀，並尋找其中的角點
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

    # 建立一個掩膜為了後面繪製角點的光流軌跡
    mask = np.zeros_like(old_frame)

    totalDst = [0]*100
    dst = [0]*100
    cnt = 0
    move = 0

    time_start = time.time()
    
    plt.ion()

    while(1):
        cnt+=1
        ret, frame = cap.read()
        if ret:
            # frame = cv2.flip(frame,1)
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 計算能夠獲取到的角點的新位置
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            if p1 is None:
                p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
                p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)


            # 選取好的角點，並篩選出舊的角點對應的新的角點
            good_new = p1[st == 1]
            good_old = p0[st == 1]
            MinLength = len(good_new)
            if MinLength < len(good_old):
                MinLength = len(good_old)

            # 繪製角點的軌跡
            for i,(new,old) in enumerate(zip(good_new,good_old)):
                a,b = new.ravel()
                c,d = old.ravel()
                print(i)
                # print(i, a, b, c, d)
                temDst = math.pow(int(math.pow((int(a)-int(c)), 2) + math.pow((int(b)-int(d)), 2)), 0.5)
                if temDst <= 10:
                    totalDst[i] += temDst
                    dst[i] = totalDst[i]/cnt

                    # Print每個點的變化率
                    print(dst[i])
                    
                    # 要抓的Range
                    if 1 < dst[i] and dst[i] < 3:
                        move = 1
                    mask = cv2.line(mask, (int(a),int(b)), (int(c),int(d)), color[i].tolist(), 2)
                    frame = cv2.circle(frame, (int(a),int(b)), 5, color[i].tolist(), -1)

            img = cv2.add(frame, mask)

            # Mac 要註解下面那行
            # cv2.imshow("frame", img)

            #  Windows 要註解這區域{
            plt.imshow(img)
            plt.pause(.01)
            plt.cla()  # clear axis
            plt.clf()
            # }

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

            # 更新當前幀和當前角點的位置
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1,1,2)

            time_end = time.time() 
            time_c = time_end - time_start

            # 設定多久重新抓觀測點 (秒單位)
            if int(time_c) == sec:
                if move == 1:
                    time_start = time_end
                    mask = np.zeros_like(old_frame)
                    totalDst = [0]*100
                    dst = [0]*100
                    cnt = 0
                    move = 0
                else:
                    return True
            
        else:
            break
    
    # Window 要註解這一區 {
    cv2.destroyAllWindows()
    plt.ioff()
    # }
    cap.release()


# "/Users/richard/Downloads/crossroad.mp4"
# Optical函示 第一個參數為影片路徑, 若設定為0則為預設鏡頭
# 第二個參數為設定幾秒觀測一次
print(OpticalFlow("/Users/richard/Downloads/crossroad.mp4", 2))