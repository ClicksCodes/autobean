# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

import datetime
from typing import Type, TypeVar, final
from .. import base
from .. import internal
from ..amount import Amount
from ..currency import Currency
from ..date import Date
from ..punctuation import Whitespace

_Self = TypeVar('_Self', bound='Price')


@internal.token_model
class PriceLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'PRICE'
    DEFAULT = 'price'


@internal.tree_model
class Price(base.RawTreeModel):
    RULE = 'price'

    _date = internal.required_field[Date]()
    _label = internal.required_field[PriceLabel]()
    _currency = internal.required_field[Currency]()
    _amount = internal.required_field[Amount]()

    raw_date = internal.required_node_property(_date)
    raw_currency = internal.required_node_property(_currency)
    raw_amount = internal.required_node_property(_amount)

    date = internal.required_date_property(raw_date)
    currency = internal.required_string_property(raw_currency)
    amount = raw_amount

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            date: Date,
            label: PriceLabel,
            currency: Currency,
            amount: Amount,
    ):
        super().__init__(token_store)
        self._date = date
        self._label = label
        self._currency = currency
        self._amount = amount

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._date.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._amount.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._date.clone(token_store, token_transformer),
            self._label.clone(token_store, token_transformer),
            self._currency.clone(token_store, token_transformer),
            self._amount.clone(token_store, token_transformer),
        )
    
    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._currency = self._currency.reattach(token_store, token_transformer)
        self._amount = self._amount.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Price)
            and self._date == other._date
            and self._label == other._label
            and self._currency == other._currency
            and self._amount == other._amount
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            currency: Currency,
            amount: Amount,
    ) -> _Self:
        label = PriceLabel.from_default()
        tokens = [
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *currency.detach(),
            Whitespace.from_default(),
            *amount.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        date.reattach(token_store)
        label.reattach(token_store)
        currency.reattach(token_store)
        amount.reattach(token_store)
        return cls(token_store, date, label, currency, amount)

    @classmethod
    def from_value(
            cls: Type[_Self],
            date: datetime.date,
            currency: str,
            amount: Amount,
    ) -> _Self:
        return cls.from_children(
            Date.from_value(date),
            Currency.from_value(currency),
            amount,
        )