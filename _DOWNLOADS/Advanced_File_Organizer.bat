@echo off
setlocal EnableExtensions DisableDelayedExpansion
title Advanced Windows File Organizer
color 0B

:MENU
cls
echo ============================================================
echo                ADVANCED FILE ORGANIZER TEKBIMBO
echo ============================================================
echo.
echo  1. Organize this folder (where this BAT is saved)
echo  2. Choose a folder
echo  3. Organize all fixed drives (careful!) OPTIONAL WAG NA TO!
echo  4. Exit
echo.
set "choice="
set /p "choice=Choose an option [1-4]: "

if "%choice%"=="1" goto CURRENT
if "%choice%"=="2" goto PICK
if "%choice%"=="3" goto ALLDRIVES
if "%choice%"=="4" goto END
echo.
echo Invalid choice. Please choose 1, 2, 3, or 4.
pause
goto MENU

:CURRENT
set "TARGET=%~dp0"
call :CONFIRM
if errorlevel 1 goto MENU
call :ORGANIZE "%TARGET%"
goto DONE

:PICK
set "TARGET="
echo.
echo Enter the full path of the folder to organize.
echo Example: D:\Downloads
set /p "TARGET=Folder path: "
if not defined TARGET goto MENU
set "TARGET=%TARGET:"=%"
if not exist "%TARGET%\." (
    echo.
    echo Folder not found: "%TARGET%"
    pause
    goto MENU
)
call :CONFIRM
if errorlevel 1 goto MENU
call :ORGANIZE "%TARGET%"
goto DONE

:ALLDRIVES
cls
echo WARNING: This option scans folders across fixed drives.
echo It skips Windows system folders, program folders, and
echo user profile AppData folders, but it can still move files
echo in other folders. Use option 2 for safer, targeted sorting.
echo.
set "confirmAll="
set /p "confirmAll=Type ALL to continue: "
if /I not "%confirmAll%"=="ALL" goto MENU

for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist "%%D:\." (
        echo.
        echo Scanning drive %%D:\
        call :WALKDRIVE "%%D:\"
    )
)
goto DONE

:CONFIRM
echo.
echo Target: "%TARGET%"
echo Files will be MOVED into category folders.
echo Existing files with the same name will be skipped.
set "confirm="
set /p "confirm=Continue? Type Y to proceed: "
if /I "%confirm%"=="Y" exit /b 0
exit /b 1

:ORGANIZE
set "TARGET=%~1"
if not exist "%TARGET%\." (
    echo Folder not found: "%TARGET%"
    exit /b
)
echo.
echo Organizing: "%TARGET%"
pushd "%TARGET%" || exit /b
for %%F in (*) do (
    if exist "%%~fF" if not "%%~aF"=="" (
        if /I not "%%~nxF"=="%~nx0" (
            call :CLASSIFY "%%~fF" "%%~xF" "%%~nxF"
        )
    )
)
popd
exit /b

:WALKDRIVE
rem Recursively visit directories while skipping common system locations.
for /D %%P in ("%~1*") do (
    if exist "%%~fP\." (
        set "skip="
        call :CHECKSKIP "%%~fP"
        if not defined skip (
            call :ORGANIZE "%%~fP"
            call :WALKDRIVE "%%~fP\"
        )
    )
)
exit /b

:CHECKSKIP
set "skip="
set "pathcheck=%~1"
for %%S in ("\Windows" "\Program Files" "\Program Files (x86)" "\ProgramData" "\$Recycle.Bin" "\System Volume Information" "\Recovery" "\PerfLogs" "\AppData") do (
    echo(%pathcheck%| findstr /I /L /E /C:%%~S >nul && set "skip=1"
)
exit /b

:CLASSIFY
set "file=%~1"
set "ext=%~2"
set "filename=%~3"
set "category=Others"

for %%E in (.jpg .jpeg .png .gif .bmp .webp .svg .tif .tiff .heic .ico .raw .jfif .avif) do if /I "%ext%"=="%%E" set "category=Pictures"
for %%E in (.mp3 .wav .flac .aac .m4a .ogg .wma .mid .midi .opus .aiff .ape) do if /I "%ext%"=="%%E" set "category=Music"
for %%E in (.mp4 .mkv .avi .mov .wmv .flv .webm .m4v .mpeg .mpg .3gp .ts .mts .m2ts) do if /I "%ext%"=="%%E" set "category=Videos"
for %%E in (.pdf .doc .docx .xls .xlsx .ppt .pptx .txt .csv .rtf .odt .ods .odp .epub) do if /I "%ext%"=="%%E" set "category=Documents"
for %%E in (.zip .rar .7z .tar .gz .bz2 .xz .tgz) do if /I "%ext%"=="%%E" set "category=Compressed"
for %%E in (.exe .msi .msp .msix .appx) do if /I "%ext%"=="%%E" set "category=Installers"
for %%E in (.bat .cmd .ps1 .py .js .html .htm .css .json .xml .php .java .cpp .c .h .sql .ts .jsx .tsx .yml .yaml .ini .cfg) do if /I "%ext%"=="%%E" set "category=Code"
for %%E in (.ttf .otf .woff .woff2) do if /I "%ext%"=="%%E" set "category=Fonts"
for %%E in (.torrent .nfo .log .dat .bak .tmp) do if /I "%ext%"=="%%E" set "category=Other Formats"

if not exist "%category%" md "%category%" 2>nul
if exist "%category%\%filename%" (
    echo SKIPPED duplicate: "%filename%"
    exit /b
)
move "%file%" "%category%\" >nul 2>&1
if errorlevel 1 (
    echo FAILED: "%filename%"
) else (
    echo Moved: "%filename%" ^> %category%
)
exit /b

:DONE
echo.
echo ============================================================
echo Finished. Review the folders and skipped/failed files above.
echo ============================================================
pause
goto MENU

:END
endlocal
exit /b
