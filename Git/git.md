# Git Basic Commands
- ### git init
- ### git add
- ### git commit
- ### git status
- ### git push
- ### git pull
- ### git clone 
- ### git checkout
- ### git rm
- ### git diff
- ### git log
- ### git branch
- ### git merge 
- ### git config
- ### git blame
- ### git branch -M main (or master)
- ### git remote add origin < url >
- ### git push -u origin main | push -f (Force)
- ### git remote set-url origin <https://githubusername@github.com...>

# Git Next Level
- ### git commit --amend -m " Message "
*En son snapshot i alinan commiti bu commit ile birlestirir.Yani commit acmaz, log tarihcesinde gozukmez. -m kullanmadan yapilirsa commitler yine birlesir ama mesaj ayni olarak kalir.*
- ### git revert < commitID >
*Commit id git log dan alinabilir.Son 7 hanesini almak yeterlidir. Yazilan Id deki commite revert edilir ancak reverted olarak log timeline inda isaretlenir.*
- ### git reset --hard < commitID >
*This command resets and deletes from log timeline every commit above specified commitID. Keeps below.*
- ### git diff < commitID >< commitID >< filename >
*If execute without filename then it shows the difference on used Branch not File.*
- ### git branch 
*Her olusan branch suan ustunde oldugun branchi referans alarak ondan dallanir.*
**git branch:** Shows the existing branches and where you at.
**git branch header:** Creates the 'header' branch but u still in master.
**git checkout header:** Now you switched from master to header.
**git checkout -b footer:** Creates 'footer' branch and immidiately switches to it.
**git branch -D footer:** Deletes the branch 'footer'.(First switch to master.)
- ### git stash
*En son aldigimiz committen itibaren yaptigimiz degisiklikleri bir kosede saklayip ihtiyacimiz oldugunda bize geri dondurur.*
**git stash list:** Olusan stash i ve nerden ne ekleneceginin listesini gosterir.
**git stash clear:** Stashi siler ve stash listi temizler.
**git stash pop:** Birden fazla kez git stash komutu kullanilmis ve stash listte birden fazla oge olabilir. Bu komut en ustteki stash kaydini geri donderir ve listeyi siler.
**git stash apply < stashID >:** Stash listten istenilen stash ogesini geri dondurur ve listeyi silmez.
- ### git merge < branchName >
*Uzerinde bulundugumuz master branchi ile verecegimiz branchi birlestirir. Her ikisi ustunde olan commitleri de birlestirir. Yani hem masterin hem birlesen branchin commitlerini ayri ayri gorebiliriz.*
**git merge --squash < branchName >:** Ustunde oldugumuz master branchinin commitleri logda gozukur < branchName > uzerinden gelecek olan commitler gozukmez Onun yerine birlesim esnasinda bir commit almamiz istenir.
**git merge --abort:** Conflict esnasinda merge u iptal etmek icin.

# Git Configuration
- ### git config --global --list or git congif -l
- ### git config --global init.defaultbranch main
- ### git config --global user.name < 'name' >
- ### git config --global user.password < 'password' >
- ### git config --global user.email < 'email' >
  