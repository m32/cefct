@echo off
if exist gen\nul del /s /q gen >nul
if not exist gen\nul mkdir gen
python.exe -B cefglue_interop_gen.py ^
--cpp-header-dir include ^
--cefglue-dir gen\ ^
--no-backup
