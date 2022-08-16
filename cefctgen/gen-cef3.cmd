@echo off
if exist gen\nul del /s /q gen >nul
if not exist gen\nul mkdir gen
set cef=../cef_binary_104.4.18+g2587cf2+chromium-104.0.5112.81_windows64
python.exe -B cefglue_interop_gen.py ^
--cpp-header-dir include ^
--cefglue-dir gen\ ^
--no-backup ^
--cef-dir %cef%
cl -Ox -MD -I %cef% cefsizes.c
cefsizes
del /q *.exp *.lib *.obj cefsizes.c cefsizes.exe
