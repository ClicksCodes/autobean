# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

import datetime
from typing import Type, TypeVar, final
from .. import base, internal
from ..account import Account
from ..date import Date
from ..punctuation import Whitespace

_Self = TypeVar('_Self', bound='Pad')


@internal.token_model
class PadLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'PAD'
    DEFAULT = 'pad'


@internal.tree_model
class Pad(base.RawTreeModel):
    RULE = 'pad'

    _date = internal.required_field[Date]()
    _label = internal.required_field[PadLabel]()
    _account = internal.required_field[Account]()
    _source_account = internal.required_field[Account]()

    raw_date = internal.required_node_property(_date)
    raw_account = internal.required_node_property(_account)
    raw_source_account = internal.required_node_property(_source_account)

    date = internal.required_date_property(raw_date)
    account = internal.required_string_property(raw_account)
    source_account = internal.required_string_property(raw_source_account)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            date: Date,
            label: PadLabel,
            account: Account,
            source_account: Account,
    ):
        super().__init__(token_store)
        self._date = date
        self._label = label
        self._account = account
        self._source_account = source_account

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._date.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._source_account.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._date.clone(token_store, token_transformer),
            self._label.clone(token_store, token_transformer),
            self._account.clone(token_store, token_transformer),
            self._source_account.clone(token_store, token_transformer),
        )

    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._account = self._account.reattach(token_store, token_transformer)
        self._source_account = self._source_account.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Pad)
            and self._date == other._date
            and self._label == other._label
            and self._account == other._account
            and self._source_account == other._source_account
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            account: Account,
            source_account: Account,
    ) -> _Self:
        label = PadLabel.from_default()
        tokens = [
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *account.detach(),
            Whitespace.from_default(),
            *source_account.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        date.reattach(token_store)
        label.reattach(token_store)
        account.reattach(token_store)
        source_account.reattach(token_store)
        return cls(token_store, date, label, account, source_account)

    @classmethod
    def from_value(
            cls: Type[_Self],
            date: datetime.date,
            account: str,
            source_account: str,
    ) -> _Self:
        return cls.from_children(
            Date.from_value(date),
            Account.from_value(account),
            Account.from_value(source_account),
        )
