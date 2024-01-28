# Git commands

## change branch name to main

```bash
git branch -M main
```
</br>

## Add remote to git

```bash
git remote add origin https://github.com/Nakul74/sample.git
```
</br>

## Add add and commit

```bash
git add . && git commit -m "sample commit"
```
</br>

## push to github

```bash
git push -u origin branch_name
```
</br>

## check remote

```bash
git remote -v
```
</br>

## create new branch and change to new branch

```bash
git checkout -b new_branch_name
```
</br>

## change branch

```bash
git checkout new_branch_name
```
</br>

## pull changes

```bash
git pull new_branch_name
```
</br>

## Delete branch

```bash
git branch -D
```
</br>

## If you are getting 403 error while pushing the code than follow below steps

* step 1: Go to below path in your github account and generate new token
- My account - Setting - Developer Setting - Personal Access Token - Generate New Token - Tokens (classic) - Generate new token (classic)

* step 2: use the below command to add origin
```bash
git remote add origin https://<token>@github.com/<username>/<repo>
```
example
```bash
git remote add origin https://xxxxx@github.com/Nakul74/xxx.git
```

* step 3: Now you can push the changes after renaming branch to main
```bash
git branch -M main
git push -u origin main
```

## common github commnds list [article link](https://github.com/joshnh/Git-Commands)

## Git bach first time setup guide [article link](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
