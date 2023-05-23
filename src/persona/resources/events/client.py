# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import PersonaEnvironment
from ...errors.bad_request_error import BadRequestError
from ...types.events_list_all_response import EventsListAllResponse
from ...types.events_retrieve_response import EventsRetrieveResponse


class EventsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def list_all(
        self,
        *,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        filter_name: typing.Optional[str] = None,
        filter_object_id: typing.Optional[str] = None,
        filter_id: typing.Optional[str] = None,
        key_inflection: typing.Optional[str] = None,
    ) -> EventsListAllResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "events"),
            params={
                "page[before]": page_before,
                "page[after]": page_after,
                "page[size]": page_size,
                "filter[name]": filter_name,
                "filter[object_id]": filter_object_id,
                "filter[id]": filter_id,
            },
            headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventsListAllResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(self, event_id: str, *, key_inflection: typing.Optional[str] = None) -> EventsRetrieveResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"events/{event_id}"),
            headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventsRetrieveResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEventsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def list_all(
        self,
        *,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        filter_name: typing.Optional[str] = None,
        filter_object_id: typing.Optional[str] = None,
        filter_id: typing.Optional[str] = None,
        key_inflection: typing.Optional[str] = None,
    ) -> EventsListAllResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "events"),
                params={
                    "page[before]": page_before,
                    "page[after]": page_after,
                    "page[size]": page_size,
                    "filter[name]": filter_name,
                    "filter[object_id]": filter_object_id,
                    "filter[id]": filter_id,
                },
                headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventsListAllResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(self, event_id: str, *, key_inflection: typing.Optional[str] = None) -> EventsRetrieveResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"events/{event_id}"),
                headers=remove_none_from_headers({"Key-Inflection": key_inflection, "Authorization": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EventsRetrieveResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
