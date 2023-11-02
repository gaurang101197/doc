# Git

## Branch and Commit

### Branch Naming Convention

`category`/`ticket`/`description`

#### Branch Category

- `feature` is for adding, refactoring or removing a feature
- `bugfix` is for fixing a bug
- `hotfix` is for changing code with a temporary solution and/or without following the usual process (usually because of an emergency)
- `test` is for experimenting outside of an issue/ticket

#### Branch Examples

- feature/issue-42/create-new-button-component
- bugfix/issue-342/button-overlap-form-on-mobile
- hotfix/**no-ref**/registration-form-not-working
- test/**no-ref**/refactor-components-with-atomic-design

### Commit Naming Convention

`category`: `commit statements separated by ;`

#### Commit Category

- `feat` is for adding a new feature
- `fix` is for fixing a bug
- `refactor` is for changing code for peformance or convenience purpose (e.g. readibility)
- `chore` is for everything else (writing documentation, formatting, adding tests, cleaning useless code etc.)

#### Commit Examples

- feat: add new button component; add new button components to templates
- fix: add the stop directive to button component to prevent propagation
- refactor: rewrite button component in TypeScript
- chore: write button documentation

## git cheatsheet

```bash
git cheery-pick commit-hash
git stash list
git stash pop stash@{1}
git stash apply stash@{1}
```

### move head to specific commit

This will destroy any local modifications.  
Don't do it if you have uncommitted work you want to keep.  
`git reset --hard commit-hash`  

Alternatively, if there's work to keep:  

```bash
git stash
git reset --hard commit-hash
git stash pop
```

### to create branch from commit

`git checkout -b old-state commit-hash`

### to checkout commit

`git checkout commit-hash`

### to checkout tag

`git checkout tags/<tag> -b <branch>`

### renaming local and remote branch

```bash
git checkout <old_name>
git branch -m <new_name>
git push <remote> <remote>/<old_name>:refs/heads/<new_name> :<old_name>
```

### merge two commits into one

```bash
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
```

### Removing the last commit

`git reset --hard HEAD^`

### Remove last n commits

`git reset --hard HEAD~n`

### If you want to "uncommit" the commits, but keep the changes around for reworking

`git reset HEAD^`

### revert specific commit

`git revert commit-id`

### [Remove a file from a Git repository without deleting it from the local filesystem](https://stackoverflow.com/questions/1143796/remove-a-file-from-a-git-repository-without-deleting-it-from-the-local-filesyste)

```bash
git rm -r --cached <your directory>
```

### [How do I find and restore a deleted file in a Git repository?](https://stackoverflow.com/questions/953481/how-do-i-find-and-restore-a-deleted-file-in-a-git-repository)

```bash
Find the last commit that affected the given path. As the file isn't in the HEAD commit, that previous commit must have deleted it.
git rev-list -n 1 HEAD -- <file_path>

Then checkout the version at the commit before, using the caret (^) symbol:
git checkout <deleting_commit>^ -- <file_path>

Or in one command, if $file is the file in question.
git checkout $(git rev-list -n 1 HEAD -- "$file")^ -- "$file"
```

### [How do I configure git to ignore some files locally?](https://stackoverflow.com/questions/1753070/how-do-i-configure-git-to-ignore-some-files-locally)

The `.git/info/exclude` file has the same format as any `.gitignore` file.  
**OR**  
`git update-index --skip-worktree <file-list>`  
Reverse it by:  
`git update-index --no-skip-worktree <file-list>`

### Divergent branches

<https://stackoverflow.com/questions/71768999/how-to-merge-when-you-get-error-hint-you-have-divergent-branches-and-need-to-s>

## References

1. <https://stackoverflow.com/questions/30590083/how-do-i-rename-both-a-git-local-and-remote-branch-name>
2. <https://gist.github.com/cutiko/0b1615c63504a940877541362cc51211>
3. <https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4?utm_source=pocket_saves>
