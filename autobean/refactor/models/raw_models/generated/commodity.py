# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

from typing import Type, TypeVar, final
from .. import base
from .. import internal
from ..currency import Currency
from ..date import Date
from ..punctuation import Whitespace

_Self = TypeVar('_Self', bound='Commodity')


@internal.token_model
class CommodityLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'COMMODITY'
    DEFAULT = 'commodity'


@internal.tree_model
class Commodity(base.RawTreeModel):
    RULE = 'commodity'

    _date = internal.required_field[Date]()
    _label = internal.required_field[CommodityLabel]()
    _currency = internal.required_field[Currency]()

    raw_date = internal.required_node_property(_date)
    raw_currency = internal.required_node_property(_currency)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            date: Date,
            label: CommodityLabel,
            currency: Currency,
    ):
        super().__init__(token_store)
        self._date = date
        self._label = label
        self._currency = currency

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._date.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._currency.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._date.clone(token_store, token_transformer),
            self._label.clone(token_store, token_transformer),
            self._currency.clone(token_store, token_transformer),
        )
    
    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._currency = self._currency.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Commodity)
            and self._date == other._date
            and self._label == other._label
            and self._currency == other._currency
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            currency: Currency,
    ) -> _Self:
        label = CommodityLabel.from_default()
        tokens = [
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *currency.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        date.reattach(token_store)
        label.reattach(token_store)
        currency.reattach(token_store)
        return cls(token_store, date, label, currency)