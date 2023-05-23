# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class BusinessLookupReport1RequestDataAttributesQuery(pydantic.BaseModel):
    registration_country_code: str = pydantic.Field(
        alias="registration-country-code",
        description=(
            "2 digit ISO code for country. Please see https://dash.readme.com/project/personaidentities/v2021-07-05/docs/country-codes\n"
        ),
    )
    registration_number: typing.Optional[str] = pydantic.Field(alias="registration-number")
    name: typing.Optional[str] = pydantic.Field(description=("Name of the business\n"))
    legal_status: typing.Optional[str] = pydantic.Field(
        alias="legal-status", description=("Legal status of business (active, inactive, unknown)\n")
    )
    legal_entity_type: typing.Optional[str] = pydantic.Field(
        alias="legal-entity-type", description=("Legal entity type; please see\n")
    )
    registration_subdivision: typing.Optional[str] = pydantic.Field(
        alias="registration-subdivision",
        description=(
            "Subdivision of the business registrar's address; for the US this will be the 2 digit state code, for CA the providence\n"
        ),
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
