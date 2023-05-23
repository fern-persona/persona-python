# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class InquiriesRetrieveResponseIncludedItemAttributes(pydantic.BaseModel):
    status: typing.Optional[str]
    created_at: typing.Optional[str] = pydantic.Field(alias="created-at")
    completed_at: typing.Optional[str] = pydantic.Field(alias="completed-at")
    country_code: typing.Optional[str] = pydantic.Field(alias="country-code")
    name_first: typing.Optional[str] = pydantic.Field(alias="name-first")
    name_middle: typing.Optional[typing.Any] = pydantic.Field(alias="name-middle")
    name_last: typing.Optional[str] = pydantic.Field(alias="name-last")
    address_street_1: typing.Optional[str] = pydantic.Field(alias="address-street-1")
    address_street_2: typing.Optional[typing.Any] = pydantic.Field(alias="address-street-2")
    address_city: typing.Optional[str] = pydantic.Field(alias="address-city")
    address_subdivision: typing.Optional[str] = pydantic.Field(alias="address-subdivision")
    address_postal_code: typing.Optional[str] = pydantic.Field(alias="address-postal-code")
    birthdate: typing.Optional[str]

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
