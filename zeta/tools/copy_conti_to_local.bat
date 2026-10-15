@echo off
chcp 65001 >nul
set PYTHONUTF8=1
rem 더블클릭하면: 최신 main을 받고(git pull) 숏드라마 콘티 md를 H:\항아리\generated\번호_이름\ 으로 복사한다.
cd /d "%~dp0..\.."
echo [1/2] git pull ...
git pull
echo.
echo [2/2] 콘티 복사 ...
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 zeta\tools\copy_conti_to_local.py %*
) else (
  python zeta\tools\copy_conti_to_local.py %*
)
echo.
pause
