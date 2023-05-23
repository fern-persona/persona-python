# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .retrieve_a_tin_database_verifications_response_data_attributes_checks_item import (
    RetrieveATinDatabaseVerificationsResponseDataAttributesChecksItem,
)


class RetrieveATinDatabaseVerificationsResponseDataAttributes(pydantic.BaseModel):
    status: typing.Optional[str]
    created_at: typing.Optional[str] = pydantic.Field(alias="created-at")
    created_at_ts: typing.Optional[int] = pydantic.Field(alias="created-at-ts")
    submitted_at: typing.Optional[str] = pydantic.Field(alias="submitted-at")
    submitted_at_ts: typing.Optional[int] = pydantic.Field(alias="submitted-at-ts")
    completed_at: typing.Optional[str] = pydantic.Field(alias="completed-at")
    completed_at_ts: typing.Optional[int] = pydantic.Field(alias="completed-at-ts")
    country_code: typing.Optional[str] = pydantic.Field(alias="country-code")
    name_first: typing.Optional[str] = pydantic.Field(alias="name-first")
    checks: typing.Optional[typing.List[RetrieveATinDatabaseVerificationsResponseDataAttributesChecksItem]]

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
