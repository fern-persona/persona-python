# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class BusinessLookupReport1ResponseDataAttributesResultItemAddressesItem(pydantic.BaseModel):
    street_1: typing.Optional[str] = pydantic.Field(alias="street-1")
    street_2: typing.Optional[typing.Any] = pydantic.Field(alias="street-2")
    city: typing.Optional[str]
    subdivision: typing.Optional[typing.Any]
    postal_code: typing.Optional[str] = pydantic.Field(alias="postal-code")
    country_code: typing.Optional[str] = pydantic.Field(alias="country-code")

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
