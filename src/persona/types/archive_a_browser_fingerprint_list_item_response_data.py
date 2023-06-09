# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .archive_a_browser_fingerprint_list_item_response_data_attributes import (
    ArchiveABrowserFingerprintListItemResponseDataAttributes,
)
from .archive_a_browser_fingerprint_list_item_response_data_relationships import (
    ArchiveABrowserFingerprintListItemResponseDataRelationships,
)


class ArchiveABrowserFingerprintListItemResponseData(pydantic.BaseModel):
    type: typing.Optional[str]
    id: typing.Optional[str]
    attributes: typing.Optional[ArchiveABrowserFingerprintListItemResponseDataAttributes]
    relationships: typing.Optional[ArchiveABrowserFingerprintListItemResponseDataRelationships]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
