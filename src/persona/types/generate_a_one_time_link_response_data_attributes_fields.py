# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .generate_a_one_time_link_response_data_attributes_fields_address_city import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsAddressCity,
)
from .generate_a_one_time_link_response_data_attributes_fields_address_postal_code import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsAddressPostalCode,
)
from .generate_a_one_time_link_response_data_attributes_fields_address_street_1 import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsAddressStreet1,
)
from .generate_a_one_time_link_response_data_attributes_fields_address_street_2 import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsAddressStreet2,
)
from .generate_a_one_time_link_response_data_attributes_fields_address_subdivision import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsAddressSubdivision,
)
from .generate_a_one_time_link_response_data_attributes_fields_birthdate import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsBirthdate,
)
from .generate_a_one_time_link_response_data_attributes_fields_email_address import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsEmailAddress,
)
from .generate_a_one_time_link_response_data_attributes_fields_identification_number import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsIdentificationNumber,
)
from .generate_a_one_time_link_response_data_attributes_fields_name_first import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsNameFirst,
)
from .generate_a_one_time_link_response_data_attributes_fields_name_last import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsNameLast,
)
from .generate_a_one_time_link_response_data_attributes_fields_name_middle import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsNameMiddle,
)
from .generate_a_one_time_link_response_data_attributes_fields_phone_number import (
    GenerateAOneTimeLinkResponseDataAttributesFieldsPhoneNumber,
)


class GenerateAOneTimeLinkResponseDataAttributesFields(pydantic.BaseModel):
    birthdate: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsBirthdate]
    name_last: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsNameLast] = pydantic.Field(
        alias="name-last"
    )
    name_first: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsNameFirst] = pydantic.Field(
        alias="name-first"
    )
    name_middle: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsNameMiddle] = pydantic.Field(
        alias="name-middle"
    )
    address_city: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsAddressCity] = pydantic.Field(
        alias="address-city"
    )
    phone_number: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsPhoneNumber] = pydantic.Field(
        alias="phone-number"
    )
    email_address: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsEmailAddress] = pydantic.Field(
        alias="email-address"
    )
    address_street_1: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsAddressStreet1] = pydantic.Field(
        alias="address-street-1"
    )
    address_street_2: typing.Optional[GenerateAOneTimeLinkResponseDataAttributesFieldsAddressStreet2] = pydantic.Field(
        alias="address-street-2"
    )
    address_postal_code: typing.Optional[
        GenerateAOneTimeLinkResponseDataAttributesFieldsAddressPostalCode
    ] = pydantic.Field(alias="address-postal-code")
    address_subdivision: typing.Optional[
        GenerateAOneTimeLinkResponseDataAttributesFieldsAddressSubdivision
    ] = pydantic.Field(alias="address-subdivision")
    identification_number: typing.Optional[
        GenerateAOneTimeLinkResponseDataAttributesFieldsIdentificationNumber
    ] = pydantic.Field(alias="identification-number")

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