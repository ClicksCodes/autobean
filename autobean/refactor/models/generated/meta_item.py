# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

from typing import Optional, Type, TypeVar, final
from .. import base, internal, meta_value_internal
from ..meta_key import MetaKey
from ..meta_value import MetaRawValue, MetaValue
from ..punctuation import Eol, Whitespace

_Self = TypeVar('_Self', bound='MetaItem')


@internal.tree_model
class MetaItem(base.RawTreeModel):
    RULE = 'meta_item'

    _key = internal.required_field[MetaKey]()
    _value = internal.optional_field[MetaRawValue](separators=(Whitespace.from_default(),))
    _eol = internal.required_field[Eol]()

    raw_key = internal.required_node_property(_key)
    raw_value = internal.optional_node_property(_value)

    key = internal.required_string_property(raw_key)
    value = meta_value_internal.optional_meta_value_property(raw_value)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            key: MetaKey,
            value: internal.Maybe[MetaRawValue],
            eol: Eol,
    ):
        super().__init__(token_store)
        self._key = key
        self._value = value
        self._eol = eol

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._key.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._eol.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._key.clone(token_store, token_transformer),
            self._value.clone(token_store, token_transformer),
            self._eol.clone(token_store, token_transformer),
        )

    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._key = self._key.reattach(token_store, token_transformer)
        self._value = self._value.reattach(token_store, token_transformer)
        self._eol = self._eol.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, MetaItem)
            and self._key == other._key
            and self._value == other._value
            and self._eol == other._eol
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            key: MetaKey,
            value: Optional[MetaRawValue],
    ) -> _Self:
        maybe_value = internal.MaybeL[MetaRawValue].from_children(value, separators=cls._value.separators)
        eol = Eol.from_default()
        tokens = [
            *key.detach(),
            *maybe_value.detach(),
            *eol.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        key.reattach(token_store)
        maybe_value.reattach(token_store)
        eol.reattach(token_store)
        return cls(token_store, key, maybe_value, eol)

    @classmethod
    def from_value(
            cls: Type[_Self],
            key: str,
            value: Optional[MetaValue | MetaRawValue],
    ) -> _Self:
        return cls.from_children(
            MetaKey.from_value(key),
            meta_value_internal.from_value(value) if value is not None else None,
        )
