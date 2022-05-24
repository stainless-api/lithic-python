# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from ..types import auth_rule
from .._models import BaseModel, NoneModel, StringModel

__all__ = ["AuthRuleListResponse"]


class AuthRuleListResponse(BaseModel):
    data: Optional[List[auth_rule.AuthRule]]
