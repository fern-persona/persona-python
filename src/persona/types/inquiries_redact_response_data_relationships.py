# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .inquiries_redact_response_data_relationships_account import InquiriesRedactResponseDataRelationshipsAccount
from .inquiries_redact_response_data_relationships_reports import InquiriesRedactResponseDataRelationshipsReports
from .inquiries_redact_response_data_relationships_template import InquiriesRedactResponseDataRelationshipsTemplate
from .inquiries_redact_response_data_relationships_verifications import (
    InquiriesRedactResponseDataRelationshipsVerifications,
)


class InquiriesRedactResponseDataRelationships(pydantic.BaseModel):
    account: typing.Optional[InquiriesRedactResponseDataRelationshipsAccount]
    template: typing.Optional[InquiriesRedactResponseDataRelationshipsTemplate]
    reports: typing.Optional[InquiriesRedactResponseDataRelationshipsReports]
    verifications: typing.Optional[InquiriesRedactResponseDataRelationshipsVerifications]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
