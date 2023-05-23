# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class GovernmentIdVerificationsCreateRequestDataAttributesBackPhotoData(pydantic.BaseModel):
    """
    Government ID photo data, must be images. Can provide more than one image and we will pick the best for processing. Can also be provided as uploaded file(s) such as with multipart/form-data requests instead of this object(s).
    """

    data: str = pydantic.Field(description=("Base64 encoded file.\n"))
    filename: str = pydantic.Field(description=("Name of file.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
