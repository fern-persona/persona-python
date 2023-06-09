# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DismissMatchesRequestDataAttributesDismissType(str, enum.Enum):
    """
    required in case of Adverse Media and Business Adverse Media. "entity" - refers to one of several individuals or businesses found by the report. "media" - refers to specific article about that "entity"
    """

    ENTITY = "entity"
    MEDIA = "media"

    def visit(self, entity: typing.Callable[[], T_Result], media: typing.Callable[[], T_Result]) -> T_Result:
        if self is DismissMatchesRequestDataAttributesDismissType.ENTITY:
            return entity()
        if self is DismissMatchesRequestDataAttributesDismissType.MEDIA:
            return media()
