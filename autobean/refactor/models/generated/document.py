# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

from typing import Iterable, Type, TypeVar, final
from .. import base, internal, meta_item_internal
from ..account import Account
from ..date import Date
from ..escaped_string import EscapedString
from ..link import Link
from ..meta_item import MetaItem
from ..punctuation import Eol, Newline, Whitespace
from ..tag import Tag

_Self = TypeVar('_Self', bound='Document')


@internal.token_model
class DocumentLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'DOCUMENT'
    DEFAULT = 'document'


@internal.tree_model
class Document(base.RawTreeModel):
    RULE = 'document'

    _date = internal.required_field[Date]()
    _label = internal.required_field[DocumentLabel]()
    _account = internal.required_field[Account]()
    _filename = internal.required_field[EscapedString]()
    _tags_links = internal.repeated_field[Link | Tag](separators=(Whitespace.from_default(),))
    _eol = internal.required_field[Eol]()
    _meta = internal.repeated_field[MetaItem](separators=(Newline.from_default(),), default_indent=(Whitespace.from_raw_text('    '),))

    raw_date = internal.required_node_property(_date)
    raw_account = internal.required_node_property(_account)
    raw_filename = internal.required_node_property(_filename)
    raw_tags_links = internal.repeated_node_property(_tags_links)
    raw_meta = meta_item_internal.repeated_raw_meta_item_property(_meta)

    date = internal.required_date_property(raw_date)
    account = internal.required_string_property(raw_account)
    filename = internal.required_string_property(raw_filename)
    meta = meta_item_internal.repeated_meta_item_property(_meta)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            date: Date,
            label: DocumentLabel,
            account: Account,
            filename: EscapedString,
            tags_links: internal.Repeated[Link | Tag],
            eol: Eol,
            meta: internal.Repeated[MetaItem],
    ):
        super().__init__(token_store)
        self._date = date
        self._label = label
        self._account = account
        self._filename = filename
        self._tags_links = tags_links
        self._eol = eol
        self._meta = meta

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._date.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._meta.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._date.clone(token_store, token_transformer),
            self._label.clone(token_store, token_transformer),
            self._account.clone(token_store, token_transformer),
            self._filename.clone(token_store, token_transformer),
            self._tags_links.clone(token_store, token_transformer),
            self._eol.clone(token_store, token_transformer),
            self._meta.clone(token_store, token_transformer),
        )

    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._account = self._account.reattach(token_store, token_transformer)
        self._filename = self._filename.reattach(token_store, token_transformer)
        self._tags_links = self._tags_links.reattach(token_store, token_transformer)
        self._eol = self._eol.reattach(token_store, token_transformer)
        self._meta = self._meta.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Document)
            and self._date == other._date
            and self._label == other._label
            and self._account == other._account
            and self._filename == other._filename
            and self._tags_links == other._tags_links
            and self._eol == other._eol
            and self._meta == other._meta
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            account: Account,
            filename: EscapedString,
            tags_links: Iterable[Link | Tag] = (),
            meta: Iterable[MetaItem] = (),
    ) -> _Self:
        label = DocumentLabel.from_default()
        repeated_tags_links = cls._tags_links.create_repeated(tags_links)
        eol = Eol.from_default()
        repeated_meta = cls._meta.create_repeated(meta)
        tokens = [
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *account.detach(),
            Whitespace.from_default(),
            *filename.detach(),
            *repeated_tags_links.detach(),
            *eol.detach(),
            *repeated_meta.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        date.reattach(token_store)
        label.reattach(token_store)
        account.reattach(token_store)
        filename.reattach(token_store)
        repeated_tags_links.reattach(token_store)
        eol.reattach(token_store)
        repeated_meta.reattach(token_store)
        return cls(token_store, date, label, account, filename, repeated_tags_links, eol, repeated_meta)
