# Branch 만들고 삭제하기

```
# git branch 만들기
git branch [branch 명]

# git branch 전환
git checkout [branch 명]

# git branch 만들고 전환을 동시에
git checkout -b [branch 명]

# git branch 제거
# 현재 branch에 있다면
git checkout master # 또는 main
git branch -d [branch 명]

# merge가 안되어있을때 제거하려면
git branch -D [branch 명]
```

# git commit 수정
```
git commit --amend
```

# 작업 중에 master와 merge하는 법
```
git checkout master
git pull origin master
git checkout [branch 명]
git merge master
```

# git reset 후 push
```
git log # 로 돌아가고 싶은 log 확인 후
git reset hard [log hash]
# 추가 작업 후/안해도 되고
git commit
git push -f origin [branch]
```
