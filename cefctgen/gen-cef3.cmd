@echo off
if exist gen\nul del /s /q gen >nul
if not exist gen\nul mkdir gen
python cefsizes.py ../cef_binary_104.4.18+g2587cf2+chromium-104.0.5112.81_windows64
cl -Ox -MD -I../cef_binary_104.4.18+g2587cf2+chromium-104.0.5112.81_windows64 sizes.c
sizes
del /q *.exp *.lib *.obj sizes.exe
python.exe -B cefglue_interop_gen.py ^
--cpp-header-dir include ^
--cefglue-dir gen\ ^
--no-backup
