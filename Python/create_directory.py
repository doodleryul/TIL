import os

directory = "폴더를 생성하고 싶은 위치 + 폴더명"
# directory가 존재하지 않으면 만들기
try:
  if not os.path.exists(directory):
    os.makedirs(directory)
    print("Create directory..")
except OSError:
  print("Error: Creating directory' + directory)
