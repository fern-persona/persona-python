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
from ...errors.bad_request_error import BadRequestError
from ...types.create_a_tin_database_verifications_request_data import CreateATinDatabaseVerificationsRequestData
from ...types.create_a_tin_database_verifications_response import CreateATinDatabaseVerificationsResponse
from ...types.retrieve_a_tin_database_verifications_response import RetrieveATinDatabaseVerificationsResponse
from ...types.submit_a_tin_database_verifications_response import SubmitATinDatabaseVerificationsResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TinDatabaseVerificationsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def create_a_tin_database_verifications(
        self,
        *,
        data: typing.Optional[CreateATinDatabaseVerificationsRequestData] = OMIT,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> CreateATinDatabaseVerificationsResponse:
        _request: typing.Dict[str, typing.Any] = {}
        if data is not OMIT:
            _request["data"] = data
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "verification/database-tins"),
            json=jsonable_encoder(_request),
            headers=remove_none_from_headers(
                {"Key-Inflection": key_inflection, "Idempotency-Key": idempotency_key, "Authorization": self.api_key}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateATinDatabaseVerificationsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def submit_a_tin_database_verifications(
        self,
        verification_id: str,
        *,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> SubmitATinDatabaseVerificationsResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"verification/database-tins/{verification_id}/submit"),
            headers=remove_none_from_headers(
                {"Key-Inflection": key_inflection, "Idempotency-Key": idempotency_key, "Authorization": self.api_key}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SubmitATinDatabaseVerificationsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_a_tin_database_verifications(
        self, verification_id: str, *, key_inflection: typing.Optional[str] = None
    ) -> RetrieveATinDatabaseVerificationsResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"verification/database-tins/{verification_id}"),
            headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RetrieveATinDatabaseVerificationsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTinDatabaseVerificationsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def create_a_tin_database_verifications(
        self,
        *,
        data: typing.Optional[CreateATinDatabaseVerificationsRequestData] = OMIT,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> CreateATinDatabaseVerificationsResponse:
        _request: typing.Dict[str, typing.Any] = {}
        if data is not OMIT:
            _request["data"] = data
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "verification/database-tins"),
                json=jsonable_encoder(_request),
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
            return pydantic.parse_obj_as(CreateATinDatabaseVerificationsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def submit_a_tin_database_verifications(
        self,
        verification_id: str,
        *,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> SubmitATinDatabaseVerificationsResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"verification/database-tins/{verification_id}/submit"
                ),
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
            return pydantic.parse_obj_as(SubmitATinDatabaseVerificationsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_a_tin_database_verifications(
        self, verification_id: str, *, key_inflection: typing.Optional[str] = None
    ) -> RetrieveATinDatabaseVerificationsResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"verification/database-tins/{verification_id}"),
                headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RetrieveATinDatabaseVerificationsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)