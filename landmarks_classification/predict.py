import math
from joblib import dump, load
import socket
import struct
poses = ['spread', 'fist', 'peace','rocknroll']

clf = load("weights_vec.joblib")

HOST, PORT = "localhost", 50888
FCOUNT = 42

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
old_prediction = -1

#converting the landmarks into normalized vectors
while True:
    recv = s.recv(FCOUNT * 4)
    recvList = list(recv)
    fnumber_list = []
    fvectors_list = []
    for i in range(0, FCOUNT * 4, 4):
        fstr = bytearray([recvList[i], recvList[i + 1], recvList[i + 2], recvList[i + 3]])
        fnumber = struct.unpack('f', fstr)
        fnumber_list.extend(fnumber)
    predict = True;
    for j in range(0, 42, 2):
        if (j in [10, 18, 26, 34]):
            div = math.sqrt((fnumber_list[j] - fnumber_list[0])**2 + (fnumber_list[j + 1] - fnumber_list[1])**2)
            if(div==0):
                predict = False
                break
            fvectors_list.extend([(fnumber_list[j] - fnumber_list[0]) / div,
            (fnumber_list[j + 1] - fnumber_list[1]) / div])
        if (j not in [8, 16, 24, 32, 40]):
            div = math.sqrt((fnumber_list[j+2] - fnumber_list[j])**2 + (fnumber_list[j + 3] - fnumber_list[j+1])**2)
            if(div==0):
                predict = False
                break
            fvectors_list.extend([(fnumber_list[j + 2] - fnumber_list[j]) / div,
            (fnumber_list[j + 3] - fnumber_list[j + 1]) / div])

    prediction = int(clf.predict([fvectors_list])[0])
    if old_prediction != prediction:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
              poses[prediction])
        old_prediction = prediction


s.send(b'Close')
s.close()
