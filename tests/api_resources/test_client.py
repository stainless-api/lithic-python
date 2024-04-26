# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import APIStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopLevel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_api_status(self, client: Lithic) -> None:
        top_level = client.api_status()
        assert_matches_type(APIStatus, top_level, path=["response"])

    @parametrize
    def test_raw_response_api_status(self, client: Lithic) -> None:
        response = client.with_raw_response.api_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(APIStatus, top_level, path=["response"])

    @parametrize
    def test_streaming_response_api_status(self, client: Lithic) -> None:
        with client.with_streaming_response.api_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(APIStatus, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopLevel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_api_status(self, async_client: AsyncLithic) -> None:
        top_level = await async_client.api_status()
        assert_matches_type(APIStatus, top_level, path=["response"])

    @parametrize
    async def test_raw_response_api_status(self, async_client: AsyncLithic) -> None:
        response = await async_client.with_raw_response.api_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(APIStatus, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_api_status(self, async_client: AsyncLithic) -> None:
        async with async_client.with_streaming_response.api_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(APIStatus, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True
