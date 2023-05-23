# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .set_status_for_a_case_response_data_relationships_accounts import (
    SetStatusForACaseResponseDataRelationshipsAccounts,
)
from .set_status_for_a_case_response_data_relationships_case_comments import (
    SetStatusForACaseResponseDataRelationshipsCaseComments,
)
from .set_status_for_a_case_response_data_relationships_case_template import (
    SetStatusForACaseResponseDataRelationshipsCaseTemplate,
)
from .set_status_for_a_case_response_data_relationships_inquiries import (
    SetStatusForACaseResponseDataRelationshipsInquiries,
)
from .set_status_for_a_case_response_data_relationships_reports import SetStatusForACaseResponseDataRelationshipsReports


class SetStatusForACaseResponseDataRelationships(pydantic.BaseModel):
    case_template: typing.Optional[SetStatusForACaseResponseDataRelationshipsCaseTemplate] = pydantic.Field(
        alias="case-template"
    )
    case_comments: typing.Optional[SetStatusForACaseResponseDataRelationshipsCaseComments] = pydantic.Field(
        alias="case-comments"
    )
    accounts: typing.Optional[SetStatusForACaseResponseDataRelationshipsAccounts]
    inquiries: typing.Optional[SetStatusForACaseResponseDataRelationshipsInquiries]
    reports: typing.Optional[SetStatusForACaseResponseDataRelationshipsReports]

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
