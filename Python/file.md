# file 읽고 쓰기
- encoding이 다른 경우 open할 때 encoding 옵션도 추가해주기
- 주로 'euc-kr'로 해결됨

# read
```python
with open('directory/file_name.txt', 'r') as f:
  lines = f.readlines()
```

# write
```python
# 한줄일 경우
with open('directory/file_name.txt', 'wt') as f:
  f.write(line)
  
# 여러줄일 경우
with open('directory/file_name.txt', 'wt') as f:
  for line in lines:
    f.write(line)
```

# file 옮기기
```python
import shutil

shutil.move('original_directory/move_file.txt', 'new_directory/move_file.txt')
```

# file 찾기
```python
from glob import glob

# mp3 파일과 wav 파일이 함께 들어있는 폴더에서 wav 파일 리스트만 가져오기
filtered_file_list = glob("*.wav")
```

# file 지우기
```python
import os

os.remove('directory/remove.txt')
```
