# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .business_lookup_report_1_response_data_attributes_result_item_addresses_item import (
    BusinessLookupReport1ResponseDataAttributesResultItemAddressesItem,
)
from .business_lookup_report_1_response_data_attributes_result_item_agent import (
    BusinessLookupReport1ResponseDataAttributesResultItemAgent,
)
from .business_lookup_report_1_response_data_attributes_result_item_identifiers_item import (
    BusinessLookupReport1ResponseDataAttributesResultItemIdentifiersItem,
)
from .business_lookup_report_1_response_data_attributes_result_item_industry_codes_item import (
    BusinessLookupReport1ResponseDataAttributesResultItemIndustryCodesItem,
)
from .business_lookup_report_1_response_data_attributes_result_item_officers_item import (
    BusinessLookupReport1ResponseDataAttributesResultItemOfficersItem,
)
from .business_lookup_report_1_response_data_attributes_result_item_registration import (
    BusinessLookupReport1ResponseDataAttributesResultItemRegistration,
)
from .business_lookup_report_1_response_data_attributes_result_item_source import (
    BusinessLookupReport1ResponseDataAttributesResultItemSource,
)


class BusinessLookupReport1ResponseDataAttributesResultItem(pydantic.BaseModel):
    registration_number: typing.Optional[str] = pydantic.Field(alias="registration-number")
    registration_country_code: typing.Optional[str] = pydantic.Field(alias="registration-country-code")
    registration_subdivision: typing.Optional[typing.Any] = pydantic.Field(alias="registration-subdivision")
    name: typing.Optional[str]
    aliases: typing.Optional[typing.List[str]]
    legal_status: typing.Optional[str] = pydantic.Field(alias="legal-status")
    legal_entity_type: typing.Optional[str] = pydantic.Field(alias="legal-entity-type")
    date_of_incorporation: typing.Optional[str] = pydantic.Field(alias="date-of-incorporation")
    identifiers: typing.Optional[typing.List[BusinessLookupReport1ResponseDataAttributesResultItemIdentifiersItem]]
    addresses: typing.Optional[typing.List[BusinessLookupReport1ResponseDataAttributesResultItemAddressesItem]]
    websites: typing.Optional[typing.List[str]]
    industry_codes: typing.Optional[
        typing.List[BusinessLookupReport1ResponseDataAttributesResultItemIndustryCodesItem]
    ] = pydantic.Field(alias="industry-codes")
    registration: typing.Optional[BusinessLookupReport1ResponseDataAttributesResultItemRegistration]
    agent: typing.Optional[BusinessLookupReport1ResponseDataAttributesResultItemAgent]
    officers: typing.Optional[typing.List[BusinessLookupReport1ResponseDataAttributesResultItemOfficersItem]]
    source: typing.Optional[BusinessLookupReport1ResponseDataAttributesResultItemSource]

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
