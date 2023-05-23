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
from ...types.documents_create_request_data import DocumentsCreateRequestData
from ...types.documents_create_response import DocumentsCreateResponse
from ...types.documents_retrieve_response import DocumentsRetrieveResponse
from ...types.documents_submit_response import DocumentsSubmitResponse
from ...types.documents_update_request_data import DocumentsUpdateRequestData
from ...types.documents_update_response import DocumentsUpdateResponse


class DocumentsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def retrieve(self, document_id: str, *, key_inflection: typing.Optional[str] = None) -> DocumentsRetrieveResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"documents/{document_id}"),
            headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentsRetrieveResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        data: DocumentsCreateRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> DocumentsCreateResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "document/generics"),
            json=jsonable_encoder({"data": data}),
            headers=remove_none_from_headers(
                {"Key-Inflection": key_inflection, "Idempotency-Key": idempotency_key, "Authorization": self.api_key}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentsCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        document_id: str,
        *,
        data: DocumentsUpdateRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> DocumentsUpdateResponse:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment.value}/", f"document/generics/{document_id}"),
            json=jsonable_encoder({"data": data}),
            headers=remove_none_from_headers(
                {"Key-Inflection": key_inflection, "Idempotency-Key": idempotency_key, "Authorization": self.api_key}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentsUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def submit(
        self,
        document_id: str,
        *,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> DocumentsSubmitResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"document/generics/{document_id}/submit"),
            headers=remove_none_from_headers(
                {"Key-Inflection": key_inflection, "Idempotency-Key": idempotency_key, "Authorization": self.api_key}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentsSubmitResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def retrieve(
        self, document_id: str, *, key_inflection: typing.Optional[str] = None
    ) -> DocumentsRetrieveResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"documents/{document_id}"),
                headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentsRetrieveResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        data: DocumentsCreateRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> DocumentsCreateResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "document/generics"),
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
            return pydantic.parse_obj_as(DocumentsCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        document_id: str,
        *,
        data: DocumentsUpdateRequestData,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> DocumentsUpdateResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment.value}/", f"document/generics/{document_id}"),
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
            return pydantic.parse_obj_as(DocumentsUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def submit(
        self,
        document_id: str,
        *,
        key_inflection: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> DocumentsSubmitResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"document/generics/{document_id}/submit"),
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
            return pydantic.parse_obj_as(DocumentsSubmitResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)