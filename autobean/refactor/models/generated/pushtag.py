# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

from typing import Type, TypeVar, final
from .. import base, internal
from ..punctuation import Whitespace
from ..tag import Tag

_Self = TypeVar('_Self', bound='Pushtag')


@internal.token_model
class PushtagLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'PUSHTAG'
    DEFAULT = 'pushtag'


@internal.tree_model
class Pushtag(base.RawTreeModel):
    RULE = 'pushtag'

    _label = internal.required_field[PushtagLabel]()
    _tag = internal.required_field[Tag]()

    raw_tag = internal.required_node_property(_tag)

    tag = internal.required_string_property(raw_tag)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            label: PushtagLabel,
            tag: Tag,
    ):
        super().__init__(token_store)
        self._label = label
        self._tag = tag

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._label.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._tag.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._label.clone(token_store, token_transformer),
            self._tag.clone(token_store, token_transformer),
        )

    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._label = self._label.reattach(token_store, token_transformer)
        self._tag = self._tag.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Pushtag)
            and self._label == other._label
            and self._tag == other._tag
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            tag: Tag,
    ) -> _Self:
        label = PushtagLabel.from_default()
        tokens = [
            *label.detach(),
            Whitespace.from_default(),
            *tag.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        label.reattach(token_store)
        tag.reattach(token_store)
        return cls(token_store, label, tag)

    @classmethod
    def from_value(
            cls: Type[_Self],
            tag: str,
    ) -> _Self:
        return cls.from_children(
            Tag.from_value(tag),
        )
