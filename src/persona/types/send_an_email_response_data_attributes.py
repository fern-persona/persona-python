# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .send_an_email_response_data_attributes_metadata import SendAnEmailResponseDataAttributesMetadata


class SendAnEmailResponseDataAttributes(pydantic.BaseModel):
    status: typing.Optional[str]
    created_at: typing.Optional[str] = pydantic.Field(alias="created-at")
    created_at_ts: typing.Optional[int] = pydantic.Field(alias="created-at-ts")
    submitted_at: typing.Optional[typing.Any] = pydantic.Field(alias="submitted-at")
    submitted_at_ts: typing.Optional[typing.Any] = pydantic.Field(alias="submitted-at-ts")
    completed_at: typing.Optional[typing.Any] = pydantic.Field(alias="completed-at")
    completed_at_ts: typing.Optional[typing.Any] = pydantic.Field(alias="completed-at-ts")
    confirmation_code: typing.Optional[str] = pydantic.Field(alias="confirmation-code")
    email_address: typing.Optional[str] = pydantic.Field(alias="email-address")
    metadata: typing.Optional[SendAnEmailResponseDataAttributesMetadata]

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