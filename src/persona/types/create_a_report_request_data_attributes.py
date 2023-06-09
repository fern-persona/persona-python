# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class CreateAReportRequestDataAttributes(pydantic.BaseModel):
    report_template_id: typing.Optional[str] = pydantic.Field(
        alias="report-template-id", description=("Report Template ID corresponding to the report you want to run\n")
    )
    addressee: typing.Optional[str]
    address_street_1: typing.Optional[str] = pydantic.Field(alias="address-street-1")
    address_street_2: typing.Optional[str] = pydantic.Field(alias="address-street-2")
    address_subdivision: typing.Optional[str] = pydantic.Field(alias="address-subdivision")
    address_city: typing.Optional[str] = pydantic.Field(alias="address-city")
    address_postal_code: typing.Optional[str] = pydantic.Field(alias="address-postal-code")
    address_country_code: typing.Optional[str] = pydantic.Field(alias="address-country-code")
    name_first: typing.Optional[str] = pydantic.Field(alias="name-first")
    name_last: typing.Optional[str] = pydantic.Field(alias="name-last")
    name_full: typing.Optional[str] = pydantic.Field(alias="name-full")
    birthdate: typing.Optional[str]
    email_address: typing.Optional[str] = pydantic.Field(alias="email-address")
    phone_number: typing.Optional[str] = pydantic.Field(alias="phone-number")
    broker_type: typing.Optional[str] = pydantic.Field(alias="broker-type")
    crd_number: typing.Optional[str] = pydantic.Field(alias="crd-number")
    firm_name: typing.Optional[str] = pydantic.Field(alias="firm-name")
    social_security_number: typing.Optional[str] = pydantic.Field(alias="social-security-number")
    country_code: typing.Optional[str] = pydantic.Field(alias="country-code")
    term: typing.Optional[str]
    reference_id: typing.Optional[str] = pydantic.Field(
        alias="reference-id", description=("(optional) Reference ID of an Account to link to this Report\n")
    )

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
