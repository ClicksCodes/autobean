# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

import decimal
from typing import Type, TypeVar, final
from .. import base
from .. import internal
from ..number_expr import NumberExpr
from ..punctuation import Whitespace

_Self = TypeVar('_Self', bound='Tolerance')


@internal.token_model
class Tilde(internal.SimpleDefaultRawTokenModel):
    RULE = 'TILDE'
    DEFAULT = '~'


@internal.tree_model
class Tolerance(base.RawTreeModel):
    RULE = 'tolerance'

    _tilde = internal.required_field[Tilde]()
    _number = internal.required_field[NumberExpr]()

    raw_number = internal.required_node_property(_number)

    number = internal.required_decimal_property(raw_number)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            tilde: Tilde,
            number: NumberExpr,
    ):
        super().__init__(token_store)
        self._tilde = tilde
        self._number = number

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._tilde.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._number.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._tilde.clone(token_store, token_transformer),
            self._number.clone(token_store, token_transformer),
        )
    
    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._tilde = self._tilde.reattach(token_store, token_transformer)
        self._number = self._number.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Tolerance)
            and self._tilde == other._tilde
            and self._number == other._number
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            number: NumberExpr,
    ) -> _Self:
        tilde = Tilde.from_default()
        tokens = [
            *tilde.detach(),
            Whitespace.from_default(),
            *number.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        tilde.reattach(token_store)
        number.reattach(token_store)
        return cls(token_store, tilde, number)

    @classmethod
    def from_value(
            cls: Type[_Self],
            number: decimal.Decimal,
    ) -> _Self:
        return cls.from_children(
            NumberExpr.from_value(number),
        )
