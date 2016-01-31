@echo off
title L2 SonicTi: Login Server Console
:start
echo ======================================================================-[ Team ]
echo.
echo Iniciando o Lineage 2 SonicTi Core Login Server.
echo Website : http://l2sonicti.wix.com/sonicti
echo Forum : http://sonictiforum.hol.es/forum/
echo Bem Vindo ao Core Server SonicTi.
echo.

java -Dfile.encoding=UTF8 -Xmx128m -XX:+UseSerialGC -XX:+AggressiveOpts -cp ./lib/*;l2jfrozen-core.jar com.l2jfrozen.loginserver.L2LoginServer

if ERRORLEVEL 2 goto restart
if ERRORLEVEL 1 goto error
goto end
:restart
echo.
echo Admin Restarted ...
ping -n 5 localhost > nul
echo.
goto start
:error
echo.
echo LoginServer terminated abnormaly
ping -n 5 localhost > nul
echo.
goto start
:end
echo.
echo LoginServer terminated
echo.
:question
set choix=q
set /p choix=Restart(r) or Quit(q)
if /i %choix%==r goto start
if /i %choix%==q goto exit
:exit
exit
pause
