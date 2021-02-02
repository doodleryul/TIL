# encoding이 다른 경우 open할 때 encoding 옵션도 추가해주기
# 주로 'euc-kr'로 해결됨
# read
with open('directory/file_name.txt', 'r') as f:
  lines = f.readlines()

# write
# 한줄일 경우
with open('directory/file_name.txt', 'wt') as f:
  f.write(line)
  
# 여러줄일 경우
with open('directory/file_name.txt', 'wt') as f:
  for line in lines:
    f.write(line)
