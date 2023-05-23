# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .business_lookup_report_1_response_data_attributes_query import BusinessLookupReport1ResponseDataAttributesQuery
from .business_lookup_report_1_response_data_attributes_result_item import (
    BusinessLookupReport1ResponseDataAttributesResultItem,
)


class BusinessLookupReport1ResponseDataAttributes(pydantic.BaseModel):
    status: typing.Optional[str]
    created_at: typing.Optional[str] = pydantic.Field(alias="created-at")
    completed_at: typing.Optional[str] = pydantic.Field(alias="completed-at")
    redacted_at: typing.Optional[typing.Any] = pydantic.Field(alias="redacted-at")
    query: typing.Optional[BusinessLookupReport1ResponseDataAttributesQuery]
    result: typing.Optional[typing.List[BusinessLookupReport1ResponseDataAttributesResultItem]]

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
