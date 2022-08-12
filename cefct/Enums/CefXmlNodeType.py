from . import enum


class CefXmlNodeType(enum.IntEnum):
    Unsupported = 0
    ProcessingInstruction = 1
    DocumentType = 2
    ElementStart = 3
    ElementEnd = 4
    Attribute = 5
    Text = 6
    CData = 7
    EntityReference = 8
    WhiteSpace = 9
    Comment = 10
