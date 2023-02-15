@echo on
title Multify Packer
cd ../../

rem Read the contents of P3D_PATH into %P3D_PATH%:
set /P P3D_PATH=<P3D_PATH

cd resources
for /D %%F IN ("*") DO %P3D_PATH%\bin\multify.exe -c -f "%%F.mf" "%%F"
cd ../
for /D %%F IN ("*") DO move "resources/%%F.mf" "dist/multifiles"
pause
