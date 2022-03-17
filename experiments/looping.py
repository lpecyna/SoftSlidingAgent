import os

for i in range(1,10):
    print("!!!!!!!!!!!!!!!!!LOOP: i: ", i, " !!!!!!!!!!!!!!!!!!!!")
    if i == 0:
        command = "python experiments/run_curl.py --log_dir './data/curl"+str(i)+"/' --seed -1 --save_video True"
    else:
        command = "python experiments/run_curl.py --log_dir './data/curl" + str(i) + "/' --seed -1 --save_video False"
    os.system(command)
