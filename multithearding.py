import threading as tr
import time 

def fun(sec):
    time.sleep(sec)
    print(f"sleeping for {sec}second")
# start= time.time()    
# fun(1)
# fun(3)
# fun(4)
# end=time.time()
# print(end-start)
start=time.time()
t1= tr.Thread(target=fun,args=[1])
t2= tr.Thread(target=fun,args=[3])
t3= tr.Thread(target=fun,args=[2])


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
end=time.time()
print(end-start)

