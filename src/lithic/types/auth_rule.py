# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthRule"]


class AuthRule(BaseModel):
    account_tokens: Optional[List[str]]
    """Array of account_token(s) identifying the accounts that the Auth Rule applies
    to.

    Note that only this field or `card_tokens` can be provided for a given Auth
    Rule.
    """

    allowed_countries: Optional[List[str]]
    """Countries in which the Auth Rule permits transactions.

    Note that Lithic maintains a list of countries in which all transactions are
    blocked; "allowing" those countries in an Auth Rule does not override the
    Lithic-wide restrictions.
    """

    allowed_mcc: Optional[List[str]]
    """Merchant category codes for which the Auth Rule permits transactions."""

    avs_type: Optional[Literal["ZIP_ONLY"]]
    """
    Address verification to confirm that postal code entered at point of transaction
    (if applicable) matches the postal code on file for a given card. Since this
    check is performed against the address submitted via the Enroll Consumer
    endpoint, it should only be used in cases where card users are enrolled with
    their own accounts. Available values:

    - `ZIP_ONLY` - AVS check is performed to confirm ZIP code entered at point of
      transaction (if applicable) matches address on file.
    """

    blocked_countries: Optional[List[str]]
    """Countries in which the Auth Rule automatically declines transactions."""

    blocked_mcc: Optional[List[str]]
    """
    Merchant category codes for which the Auth Rule automatically declines
    transactions.
    """

    card_tokens: Optional[List[str]]
    """Array of card_token(s) identifying the cards that the Auth Rule applies to.

    Note that only this field or `account_tokens` can be provided for a given Auth
    Rule.
    """

    program_level: Optional[bool]
    """Boolean indicating whether the Auth Rule is applied at the program level."""