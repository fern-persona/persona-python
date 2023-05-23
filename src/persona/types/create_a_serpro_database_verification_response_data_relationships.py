# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .create_a_serpro_database_verification_response_data_relationships_inquiry import (
    CreateASerproDatabaseVerificationResponseDataRelationshipsInquiry,
)
from .create_a_serpro_database_verification_response_data_relationships_selfie import (
    CreateASerproDatabaseVerificationResponseDataRelationshipsSelfie,
)


class CreateASerproDatabaseVerificationResponseDataRelationships(pydantic.BaseModel):
    inquiry: typing.Optional[CreateASerproDatabaseVerificationResponseDataRelationshipsInquiry]
    selfie: typing.Optional[CreateASerproDatabaseVerificationResponseDataRelationshipsSelfie]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
