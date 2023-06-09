# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .retrieve_an_api_log_response_data_attributes_request_get_params import (
    RetrieveAnApiLogResponseDataAttributesRequestGetParams,
)
from .retrieve_an_api_log_response_data_attributes_request_headers import (
    RetrieveAnApiLogResponseDataAttributesRequestHeaders,
)
from .retrieve_an_api_log_response_data_attributes_request_post_params import (
    RetrieveAnApiLogResponseDataAttributesRequestPostParams,
)


class RetrieveAnApiLogResponseDataAttributesRequest(pydantic.BaseModel):
    method: typing.Optional[str]
    path: typing.Optional[str]
    headers: typing.Optional[RetrieveAnApiLogResponseDataAttributesRequestHeaders]
    get_params: typing.Optional[RetrieveAnApiLogResponseDataAttributesRequestGetParams] = pydantic.Field(
        alias="get-params"
    )
    post_params: typing.Optional[RetrieveAnApiLogResponseDataAttributesRequestPostParams] = pydantic.Field(
        alias="post-params"
    )
    ip_address: typing.Optional[str] = pydantic.Field(alias="ip-address")

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
