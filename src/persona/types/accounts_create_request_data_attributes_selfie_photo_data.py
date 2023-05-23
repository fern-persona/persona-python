# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class AccountsCreateRequestDataAttributesSelfiePhotoData(pydantic.BaseModel):
    """
    Selfie photo data, must be an image. Can also be provided as an uploaded file such as with multipart/form-data requests instead of this object.
    """

    data: typing.Optional[str] = pydantic.Field(description=("Base64 encoded image\n"))
    filename: typing.Optional[str] = pydantic.Field(description=("Name of the image\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
