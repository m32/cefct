cl /MP /GS /W4 /wd"4100" /wd"4127" /wd"4244" /wd"4324" /wd"4481" /wd"4512" /wd"4701" /wd"4702" /wd"4996" /Gy ^
/Zc:wchar_t /I"..\cef_binary_102.0.3+g53d4ce9+chromium-102.0.5005.40_windows64_beta" ^
/Zi /Gm- /Od /Ob0 /Zc:inline /fp:precise /D "_UNICODE" /D "UNICODE" /D "WIN32" ^
/D "_WINDOWS" /D "__STDC_CONSTANT_MACROS" /D "__STDC_FORMAT_MACROS" /D "_WIN32" /D "WINVER=0x0601" ^
/D "_WIN32_WINNT=0x601" /D "NOMINMAX" /D "WIN32_LEAN_AND_MEAN" /D "_HAS_EXCEPTIONS=0" /D "PSAPI_VERSION=1" ^
/D "CEF_USE_SANDBOX" /D "CEF_USE_ATL" /D "_HAS_ITERATOR_DEBUGGING=0" /D "CMAKE_INTDIR=\"Debug\"" ^
/errorReport:prompt /WX /Zc:forScope /RTC1 /GR- /Gd /MTd /EHsc /nologo ^
pyhelper.cpp util_win.cpp ^
..\bin\libcef.lib ^
..\bin\libcef_dll_wrapper.lib ^
..\bin\cef_sandbox.lib ^
comctl32.lib gdi32.lib rpcrt4.lib shlwapi.lib ws2_32.lib d3d11.lib glu32.lib imm32.lib opengl32.lib oleacc.lib ^
Advapi32.lib dbghelp.lib Delayimp.lib OleAut32.lib PowrProf.lib Propsys.lib psapi.lib SetupAPI.lib ^
Shell32.lib version.lib wbemuuid.lib winmm.lib kernel32.lib user32.lib gdi32.lib winspool.lib ^
shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib
rem del /q *.exp *.lib *.obj
mt.exe -manifest pyhelper.exe.manifest -outputresource:pyhelper.exe;1
rem mt.exe -manifest MyLibrary.dll.manifest -outputresource:MyLibrary.dll;2
