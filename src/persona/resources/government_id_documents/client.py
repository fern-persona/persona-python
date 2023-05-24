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
from ...types.create_a_government_id_document_request_data import CreateAGovernmentIdDocumentRequestData
from ...types.create_a_government_id_document_response import CreateAGovernmentIdDocumentResponse
from ...types.submit_a_government_id_document_response import SubmitAGovernmentIdDocumentResponse
from ...types.update_a_government_id_document_request_data import UpdateAGovernmentIdDocumentRequestData
from ...types.update_a_government_id_document_response import UpdateAGovernmentIdDocumentResponse


class GovernmentIdDocumentsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def create_a_government_id_document(
        self,
        *,
        data: CreateAGovernmentIdDocumentRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> CreateAGovernmentIdDocumentResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "document/government-ids"),
            json=jsonable_encoder({"data": data}),
            headers=remove_none_from_headers(
                {
                    "Key-Inflection": key_inflection,
                    "Idempotency-Key": idempotency_key,
                    "Authorization": f"Bearer  {self.api_key}",
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateAGovernmentIdDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_a_government_id_document(
        self,
        document_id: str,
        *,
        data: UpdateAGovernmentIdDocumentRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> UpdateAGovernmentIdDocumentResponse:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment.value}/", f"document/government-ids/{document_id}"),
            json=jsonable_encoder({"data": data}),
            headers=remove_none_from_headers(
                {
                    "Key-Inflection": key_inflection,
                    "Idempotency-Key": idempotency_key,
                    "Authorization": f"Bearer  {self.api_key}",
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateAGovernmentIdDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def submit_a_government_id_document(
        self,
        document_id: str,
        *,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> SubmitAGovernmentIdDocumentResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"document/government-ids/{document_id}/submit"),
            headers=remove_none_from_headers(
                {
                    "Key-Inflection": key_inflection,
                    "Idempotency-Key": idempotency_key,
                    "Authorization": f"Bearer  {self.api_key}",
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SubmitAGovernmentIdDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGovernmentIdDocumentsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def create_a_government_id_document(
        self,
        *,
        data: CreateAGovernmentIdDocumentRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> CreateAGovernmentIdDocumentResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "document/government-ids"),
                json=jsonable_encoder({"data": data}),
                headers=remove_none_from_headers(
                    {
                        "Key-Inflection": key_inflection,
                        "Idempotency-Key": idempotency_key,
                        "Authorization": f"Bearer  {self.api_key}",
                    }
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateAGovernmentIdDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_a_government_id_document(
        self,
        document_id: str,
        *,
        data: UpdateAGovernmentIdDocumentRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> UpdateAGovernmentIdDocumentResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment.value}/", f"document/government-ids/{document_id}"),
                json=jsonable_encoder({"data": data}),
                headers=remove_none_from_headers(
                    {
                        "Key-Inflection": key_inflection,
                        "Idempotency-Key": idempotency_key,
                        "Authorization": f"Bearer  {self.api_key}",
                    }
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateAGovernmentIdDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def submit_a_government_id_document(
        self,
        document_id: str,
        *,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> SubmitAGovernmentIdDocumentResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"document/government-ids/{document_id}/submit"),
                headers=remove_none_from_headers(
                    {
                        "Key-Inflection": key_inflection,
                        "Idempotency-Key": idempotency_key,
                        "Authorization": f"Bearer  {self.api_key}",
                    }
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SubmitAGovernmentIdDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
