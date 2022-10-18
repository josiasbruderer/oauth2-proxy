@echo off
::
:: logrotate.bat - Log rotation for windows
::
:: Usage: logrotate.bat filename maxfilecount [maxfilesize]
::
::   filename    : The file name to rotate.
::   maxfilecount: Number of backup files.
::   maxfilesize : Rotated if the size of file exceeds specified size.
::                 (Default is 0. Unit notation is available (K, M and G))
::
:: Example:
::   logrotate.bat path\to\file 1
::     The file is renamed to path\to\file.1.
::     The file path\to\file.1 is deleted if exists.
::   logrotate.bat path\to\file 100 128
::     The file is rotated from path\to\file.1 to file\to\file.100
::     if the size exeeds 128 bytes.
::   logrotate.bat path\to\file 10 10M
::     The file is rotated from path\to\file.1 to file\to\file.10
::     if the size exeeds 10 Mega-bytes.
::
:: Copyright © 2015 Urin. Licensed under MIT.
::
setlocal enabledelayedexpansion

if "%~1" == "" (exit /b 1) else (set file=%~1)
if "%~2" == "" (exit /b 1) else (set /a maxfilecount=%~2)
if "%~3" == "" (set /a maxfilesize=0) else (set /a maxfilesize=%~3)

if not "%maxfilesize%" == "%maxfilesize:K=%" (
  set /a maxfilesize=%maxfilesize:K= * 1024%
)
if not "%maxfilesize%" == "%maxfilesize:M=%" (
  set /a maxfilesize=%maxfilesize:M= * 1048576%
)
if not "%maxfilesize%" == "%maxfilesize:G=%" (
  set /a maxfilesize=%maxfilesize:G= * 1073741824%
)

if exist "%file%" (
  for %%F in ("%file%") do (
    set filename=%%~nxF
    set size=%%~zF
  )
  if !size! geq %maxfilesize% (
    for /l %%i in (%maxfilecount%,-1,2) do (
      set /a old=%%i - 1
      if exist "%file%.!old!" (move /y "%file%.!old!" "%file%.%%i" > nul)
    )
    rename "%file%" "!filename!.1" > nul
  )
)

endlocal
