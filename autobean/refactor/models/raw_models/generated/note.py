# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

from typing import Type, TypeVar, final
from .. import base
from .. import internal
from ..account import Account
from ..date import Date
from ..escaped_string import EscapedString
from ..punctuation import Whitespace

_Self = TypeVar('_Self', bound='Note')


@internal.token_model
class NoteLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'NOTE'
    DEFAULT = 'note'


@internal.tree_model
class Note(base.RawTreeModel):
    RULE = 'note'

    _date = internal.required_field[Date]()
    _label = internal.required_field[NoteLabel]()
    _account = internal.required_field[Account]()
    _comment = internal.required_field[EscapedString]()

    raw_date = internal.required_node_property(_date)
    raw_account = internal.required_node_property(_account)
    raw_comment = internal.required_node_property(_comment)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            date: Date,
            label: NoteLabel,
            account: Account,
            comment: EscapedString,
    ):
        super().__init__(token_store)
        self._date = date
        self._label = label
        self._account = account
        self._comment = comment

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._date.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._comment.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._date.clone(token_store, token_transformer),
            self._label.clone(token_store, token_transformer),
            self._account.clone(token_store, token_transformer),
            self._comment.clone(token_store, token_transformer),
        )
    
    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._account = self._account.reattach(token_store, token_transformer)
        self._comment = self._comment.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Note)
            and self._date == other._date
            and self._label == other._label
            and self._account == other._account
            and self._comment == other._comment
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            account: Account,
            comment: EscapedString,
    ) -> _Self:
        label = NoteLabel.from_default()
        tokens = [
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *account.detach(),
            Whitespace.from_default(),
            *comment.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        date.reattach(token_store)
        label.reattach(token_store)
        account.reattach(token_store)
        comment.reattach(token_store)
        return cls(token_store, date, label, account, comment)
