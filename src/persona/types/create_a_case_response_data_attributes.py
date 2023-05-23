# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class CreateACaseResponseDataAttributes(pydantic.BaseModel):
    status: typing.Optional[str]
    name: typing.Optional[str]
    resolution: typing.Optional[typing.Any]
    created_at: typing.Optional[str] = pydantic.Field(alias="created-at")
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated-at")
    assigned_at: typing.Optional[typing.Any] = pydantic.Field(alias="assigned-at")
    resolved_at: typing.Optional[typing.Any] = pydantic.Field(alias="resolved-at")
    creator_id: typing.Optional[typing.Any] = pydantic.Field(alias="creator-id")
    creator_type: typing.Optional[typing.Any] = pydantic.Field(alias="creator-type")
    assignee_id: typing.Optional[typing.Any] = pydantic.Field(alias="assignee-id")
    resolver_id: typing.Optional[typing.Any] = pydantic.Field(alias="resolver-id")
    resolver_type: typing.Optional[typing.Any] = pydantic.Field(alias="resolver-type")
    updater_id: typing.Optional[typing.Any] = pydantic.Field(alias="updater-id")
    updater_type: typing.Optional[typing.Any] = pydantic.Field(alias="updater-type")
    tags: typing.Optional[typing.List[typing.Any]]

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
