
# Persona Python Library

[![pypi](https://img.shields.io/pypi/v/fern-persona.svg)](https://pypi.python.org/pypi/fern-persona)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Documentation

API documentation is available [here](https://docs.withpersona.com/reference/introduction).

## Installation

Add this dependency to your project's build file:

```bash
pip install fern-persona
# or
poetry add fern-persona
```

## Usage

```python
from persona.client import Persona

persona_client = Persona(api_key="MY_API_KEY")
```

## Async client

This SDK also includes an async client, which supports the `await` syntax:

```python
from persona.client import AsyncPersona

persona_client = AsyncPersona(api_key="MY_API_KEY")
```

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
