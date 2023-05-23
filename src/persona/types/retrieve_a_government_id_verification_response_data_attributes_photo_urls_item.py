# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class RetrieveAGovernmentIdVerificationResponseDataAttributesPhotoUrlsItem(pydantic.BaseModel):
    page: typing.Optional[str]
    url: typing.Optional[str]
    normalized_url: typing.Optional[str] = pydantic.Field(alias="normalized-url")
    original_urls: typing.Optional[typing.List[str]] = pydantic.Field(alias="original-urls")
    byte_size: typing.Optional[int] = pydantic.Field(alias="byte-size")

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
