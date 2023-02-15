@echo on
title Update Packer
cd ../../

rem Read the contents of P3D_PATH into %P3D_PATH%:
set /P P3D_PATH=<P3D_PATH

cd update
cd win32
%P3D_PATH%\bin\multify.exe -c -f "phase_1.mf" phase_1
%P3D_PATH%\bin\multify.exe -c -f "phase_2.mf" phase_2

cd ../../
move "update\win32\phase_1.mf" "dist\sysfiles\win32"
move "update\win32\phase_2.mf" "dist\sysfiles\win32"

pause
