set -e

date1=$(date +"%s")

echo "==> Setup"

rm -rf pythonbook.wiki || exit 0;

echo "==> Make"

make latexpdf

echo "==> Clone"

git config user.name "Travis CI"
git config user.email ${GH_EMAIL}

git clone https://github.com/dwjoyce/pythonbook.wiki.git

echo "==> Move"

cp build/latex/pythonbook.pdf pythonbook.wiki/

msg="Update to '`git log -1 --oneline`'"

cd pythonbook.wiki

echo "==> Commit"

git config user.name "Travis CI"
git config user.email ${GH_EMAIL}

git add pythonbook.pdf
git commit -m "$msg"

echo "==> Push"

git push https://matsjoyce:${GH_TOKEN}@github.com/dwjoyce/pythonbook.wiki.git master

echo "==> Done!"

date2=$(date +"%s")
diff=$(($date2-$date1))
echo "==> $(($diff / 60)) minutes and $(($diff % 60)) seconds elapsed"