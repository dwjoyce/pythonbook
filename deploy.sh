rm -rf pythonbook.wiki || exit 0;

make latexpdf

git clone https://github.com/dwjoyce/pythonbook.wiki.git

git config user.name "Travis CI"
git config user.email ${GH_EMAIL}

cp build/latex/pythonbook.pdf pythonbook.wiki/

msg="Update to '`git log -1 --oneline`'"

cd pythonbook.wiki

git add pythonbook.pdf
git commit -m "$msg"
git push https://matsjoyce:${GH_TOKEN}@github.com/dwjoyce/pythonbook.wiki.git
