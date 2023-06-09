# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .update_a_government_id_verification_response_data_attributes import (
    UpdateAGovernmentIdVerificationResponseDataAttributes,
)
from .update_a_government_id_verification_response_data_relationships import (
    UpdateAGovernmentIdVerificationResponseDataRelationships,
)


class UpdateAGovernmentIdVerificationResponseData(pydantic.BaseModel):
    type: typing.Optional[str]
    id: typing.Optional[str]
    attributes: typing.Optional[UpdateAGovernmentIdVerificationResponseDataAttributes]
    relationships: typing.Optional[UpdateAGovernmentIdVerificationResponseDataRelationships]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
