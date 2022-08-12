from . import enum


class CefColorModel(enum.IntEnum):
    Unknown = 0
    Gray = 1
    Color = 2
    Cmyk = 3
    Cmy = 4
    Kcmy = 5
    Cmy_K = 6
    Black = 7
    Grayscale = 8
    Rgb = 9
    Rgb16 = 10
    Rgba = 11

    ColorMode_Color = 12
    ColorMode_Monochrome = 13

    HP_Color_Color = 14
    HP_Color_Black = 15

    PrintoutMode_Normal = 16
    PrintoutMode_Normal_Gray = 17

    ProcessColorModel_Cmyk = 18
    ProcessColorModel_Greyscale = 19
    ProcessColorModel_Rgb = 20
