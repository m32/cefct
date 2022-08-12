from . import enum


class CefMenuId(enum.IntEnum):
    Back = 100
    Forward = 101
    Reload = 102
    ReloadNoCache = 103
    StopLoad = 104
    Undo = 110
    Redo = 111
    Cut = 112
    Copy = 113
    Paste = 114
    Delete = 115
    SelectAll = 116
    Find = 130
    Print = 131
    ViewSource = 132
    SpellcheckSuggestion0 = 200
    SpellcheckSuggestion1 = 201
    SpellcheckSuggestion2 = 202
    SpellcheckSuggestion3 = 203
    SpellcheckSuggestion4 = 204
    SpellcheckSuggestionLast = 204
    NoSpellingSuggestions = 205
    AddToDictionary = 206
    CustomFirst = 220
    CustomLast = 250
    UserFirst = 26500
    UserLast = 28500
