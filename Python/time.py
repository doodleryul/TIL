from time import time

# 측정 시작시간
start_time = time()

# 시간을 측정하고 싶은 코드
...

# 코드 실행 후 걸린 시간
end_time = time()
print("Running time : {}".format(end_time - start_time))
