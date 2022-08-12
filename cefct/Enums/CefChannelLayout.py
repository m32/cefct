from . import enum


class CefChannelLayout(enum.IntEnum):
    CNone = 0
    Unsupported = 1
    Mono = 2
    Stereo = 3
    Layout_2_1 = 4
    Surround = 5
    Layout_4_0 = 6
    Layout_2_2 = 7
    Quad = 8
    Layout_5_0 = 9
    Layout_5_1 = 10
    Layout_5_0_Back = 11
    Layout_5_1_Back = 12
    Layout_7_0 = 13
    Layout_7_1 = 14
    Layout_7_1_Wide = 15
    Layout_Stereo_Downmix = 16
    Layout_2Point1 = 17
    Layout_3_1 = 18
    Layout_4_1 = 19
    Layout_6_0 = 20
    Layout_6_0_Front = 21
    Layout_Hexagonal = 22
    Layout_6_1 = 23
    Layout_6_1_Back = 24
    Layout_6_1_Front = 25
    Layout_7_0_Front = 26
    Layout_7_1_Wide_Back = 27
    Layout_Octagonal = 28
    Discrete = 29
    StereoAndKeyboardMic = 30
    Layout_4_1_Quad_Side = 31
    Bitstream = 32
