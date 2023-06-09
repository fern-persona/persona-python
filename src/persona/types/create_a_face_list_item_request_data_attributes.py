# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .create_a_face_list_item_request_data_attributes_face_photo import (
    CreateAFaceListItemRequestDataAttributesFacePhoto,
)


class CreateAFaceListItemRequestDataAttributes(pydantic.BaseModel):
    list_id: typing.Optional[str] = pydantic.Field(
        alias="list-id", description=("ID of the list to add this item to. List must be a Face List.\n")
    )
    face_photo: typing.Optional[CreateAFaceListItemRequestDataAttributesFacePhoto] = pydantic.Field(alias="face-photo")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
