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
from ...types.create_a_workflow_run_request_data import CreateAWorkflowRunRequestData
from ...types.create_a_workflow_run_response import CreateAWorkflowRunResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WorkflowsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def create_a_workflow_run(
        self,
        workflow_id: str,
        *,
        data: typing.Optional[CreateAWorkflowRunRequestData] = OMIT,
        key_inflection: typing.Optional[str] = None,
    ) -> CreateAWorkflowRunResponse:
        _request: typing.Dict[str, typing.Any] = {}
        if data is not OMIT:
            _request["data"] = data
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"workflows/{workflow_id}/trigger"),
            json=jsonable_encoder(_request),
            headers=remove_none_from_headers(
                {"Key-Inflection": key_inflection, "Authorization": f"Bearer  {self.api_key}"}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateAWorkflowRunResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWorkflowsClient:
    def __init__(self, *, environment: PersonaEnvironment = PersonaEnvironment.DEFAULT, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def create_a_workflow_run(
        self,
        workflow_id: str,
        *,
        data: typing.Optional[CreateAWorkflowRunRequestData] = OMIT,
        key_inflection: typing.Optional[str] = None,
    ) -> CreateAWorkflowRunResponse:
        _request: typing.Dict[str, typing.Any] = {}
        if data is not OMIT:
            _request["data"] = data
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"workflows/{workflow_id}/trigger"),
                json=jsonable_encoder(_request),
                headers=remove_none_from_headers(
                    {"Key-Inflection": key_inflection, "Authorization": f"Bearer  {self.api_key}"}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateAWorkflowRunResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
