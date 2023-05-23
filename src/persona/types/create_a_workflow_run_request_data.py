# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .create_a_workflow_run_request_data_attributes import CreateAWorkflowRunRequestDataAttributes


class CreateAWorkflowRunRequestData(pydantic.BaseModel):
    """
    Matches the trigger payload schema defined by the Workflow version
    """

    attributes: typing.Optional[CreateAWorkflowRunRequestDataAttributes] = pydantic.Field(
        description=("Matches the trigger payload schema defined by the workflow version\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
