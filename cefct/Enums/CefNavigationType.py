from . import enum


class CefNavigationType(enum.IntEnum):
    LinkClicked = 0
    FormSubmitted = 1
    BackForward = 2
    Reload = 3
    FormResubmitted = 4
    Other = 5
