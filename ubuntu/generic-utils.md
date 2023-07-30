# Day to day useful commands

## [Replace each newline (\n) with a space] (https://stackoverflow.com/questions/1251999/how-can-i-replace-each-newline-n-with-a-space-using-sed)
`sed ':a;N;$!ba;s/\n/ /g' file`

## Remove new line and convert multiple space into one
`cat file | xargs`
