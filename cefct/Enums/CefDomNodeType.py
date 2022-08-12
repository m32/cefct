from . import enum


class CefDomNodeType(enum.IntEnum):
    Unsupported = 0
    Element = 1
    Attribute = 2
    Text = 3
    CDataSection = 4
    ProcessingInstruction = 5
    Comment = 6
    Document = 7
    DocumentType = 8
    DocumentFragment = 9

