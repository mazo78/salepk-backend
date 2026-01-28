@echo off
E:
cd \salepk-backend
echo GitHub par data upload ho raha hai...
git add .
git commit -m "Auto Update: %date% %time%"
git push origin main
echo Upload mukammal ho gaya!
pause