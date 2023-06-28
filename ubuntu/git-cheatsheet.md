# git cheatsheet

```bash
git cheery-pick commit-hash

# This will destroy any local modifications.
# Don't do it if you have uncommitted work you want to keep.
git reset --hard commit-hash
# Alternatively, if there's work to keep:
git stash
git reset --hard commit-hash
git stash pop

# to create branch from commit
git checkout -b old-state commit-hash

# to checkout commit
git checkout commit-hash

# to checkout tag
git checkout tags/<tag> -b <branch>


# renaming local and remote branch
git checkout <old_name>
git branch -m <new_name>
git push <remote> <remote>/<old_name>:refs/heads/<new_name> :<old_name>


# merge two commits into one
git rebase --interactive HEAD~2
## pick b76d157 b
## pick a931ac7 c
## ------
## pick   b76d157 b
## squash a931ac7 c
## ------
## save-quitting your editor, you'll get another editor whose contents are
## # This is a combination of 2 commits.
## # The first commit's message is:
## b
## # This is the 2nd commit message:
## c


# Removing the last commit
git reset --hard HEAD^
# remove last n commits
git reset --hard HEAD~n
# If you want to "uncommit" the commits, but keep the changes around for reworking
git reset HEAD^ 
```


## References
1. https://stackoverflow.com/questions/30590083/how-do-i-rename-both-a-git-local-and-remote-branch-name
2. https://gist.github.com/cutiko/0b1615c63504a940877541362cc51211