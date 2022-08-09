# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

from typing import TYPE_CHECKING, Type, TypeVar, final
from .. import base, internal
from ..punctuation import Whitespace
if TYPE_CHECKING:
  from ..number_atom_expr import NumberAtomExpr

_Self = TypeVar('_Self', bound='NumberUnaryExpr')


@internal.token_model
class UnaryOp(internal.SimpleRawTokenModel):
    RULE = 'UNARY_OP'


@internal.tree_model
class NumberUnaryExpr(base.RawTreeModel):
    RULE = 'number_unary_expr'

    _unary_op = internal.required_field[UnaryOp]()
    _operand = internal.required_field['NumberAtomExpr']()

    raw_unary_op = internal.required_node_property(_unary_op)
    raw_operand = internal.required_node_property(_operand)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            unary_op: UnaryOp,
            operand: 'NumberAtomExpr',
    ):
        super().__init__(token_store)
        self._unary_op = unary_op
        self._operand = operand

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._unary_op.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._operand.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._unary_op.clone(token_store, token_transformer),
            self._operand.clone(token_store, token_transformer),
        )

    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._unary_op = self._unary_op.reattach(token_store, token_transformer)
        self._operand = self._operand.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, NumberUnaryExpr)
            and self._unary_op == other._unary_op
            and self._operand == other._operand
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            unary_op: UnaryOp,
            operand: 'NumberAtomExpr',
    ) -> _Self:
        tokens = [
            *unary_op.detach(),
            Whitespace.from_default(),
            *operand.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        unary_op.reattach(token_store)
        operand.reattach(token_store)
        return cls(token_store, unary_op, operand)
