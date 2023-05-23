# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import PersonaEnvironment
from ...types.phone_number_verifications_create_request_data import PhoneNumberVerificationsCreateRequestData
from ...types.phone_number_verifications_create_response import PhoneNumberVerificationsCreateResponse


class PhoneNumberVerificationsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def create(
        self,
        *,
        data: PhoneNumberVerificationsCreateRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> PhoneNumberVerificationsCreateResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "verification/phone-numbers"),
            json=jsonable_encoder({"data": data}),
            headers=remove_none_from_headers(
                {"Key-Inflection": key_inflection, "Idempotency-Key": idempotency_key, "Authorization": self.api_key}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumberVerificationsCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPhoneNumberVerificationsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def create(
        self,
        *,
        data: PhoneNumberVerificationsCreateRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> PhoneNumberVerificationsCreateResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "verification/phone-numbers"),
                json=jsonable_encoder({"data": data}),
                headers=remove_none_from_headers(
                    {
                        "Key-Inflection": key_inflection,
                        "Idempotency-Key": idempotency_key,
                        "Authorization": self.api_key,
                    }
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumberVerificationsCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
