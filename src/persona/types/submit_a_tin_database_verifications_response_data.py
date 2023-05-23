# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .submit_a_tin_database_verifications_response_data_attributes import (
    SubmitATinDatabaseVerificationsResponseDataAttributes,
)
from .submit_a_tin_database_verifications_response_data_relationships import (
    SubmitATinDatabaseVerificationsResponseDataRelationships,
)


class SubmitATinDatabaseVerificationsResponseData(pydantic.BaseModel):
    type: typing.Optional[str]
    id: typing.Optional[str]
    attributes: typing.Optional[SubmitATinDatabaseVerificationsResponseDataAttributes]
    relationships: typing.Optional[SubmitATinDatabaseVerificationsResponseDataRelationships]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
