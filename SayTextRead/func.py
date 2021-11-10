import subprocess
import time
# import numpy as np
# import collections
# from datetime import timedelta

def read_text(data,readspeed,volume=0.1):
    engine = pyttsx3.init()
    engine.setProperty('rate', int(readspeed))
    engine.setProperty('volume',volume)
    engine.say(data)
    engine.runAndWait()
    # pyttsx3.speak(data)
    # engine.stop()
    return


def saytextread(filenames,use_say=True,readspeed=210,voicetype="Kyoko"):
    if not use_say:
        import pyttsx3
    start_all = time.time()
    for idxfile,filename in enumerate(filenames):
        f = open(filename, 'r')
        datas = f.read().replace('．', '。').replace('，', '、').split('\n\n')
        for idxdata,data in enumerate(datas):
            # counter = collections.Counter(data.split())
            # wordlist = counter.most_common()
            # print("word count:",np.sum([(wordlist[idx][1]) for idx in range(len(wordlist))]))
            start_each = time.time()
            if use_say:
                voicetype="Kyoko" #Japanese
                # voicetype="Alex" #US English
                # voicetype="Karen" #AU English
                readspeed_reference=210
                subprocess.call('say -v ' + voicetype + ' -r ' + str(readspeed) + ' "' + "[[volm 0]]"+data + '"', shell=True)
            else:
                readspeed_reference="210" #pyttsx3 #pyttsx3 max 720
                read_text(data,readspeed)
            nowtime=time.time()
            elapsed_time = nowtime - start_each
            elapsed_time_all = nowtime - start_all
            print(idxfile,idxdata,": time:{0}m{1}s".format(int(elapsed_time*float(readspeed)/float(readspeed_reference)//60),int(elapsed_time%60)),": elapsed time:{0}m{1}s".format(int(elapsed_time_all*float(readspeed)/float(readspeed_reference)//60),int(elapsed_time_all*float(readspeed)/float(readspeed_reference)%60)),data[0:20])
    return
