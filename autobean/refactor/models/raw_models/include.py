from autobean.refactor import token_store as token_store_lib
from . import base
from . import escaped_string
from . import internal


@base.token_model
class IncludeLabel(base.RawTokenModel):
    RULE = 'INCLUDE'


@base.tree_model
class Include(base.RawTreeModel):
    RULE = 'include'

    def __init__(self, token_store: token_store_lib.TokenStore, label: IncludeLabel, filename: escaped_string.EscapedString):
        super().__init__(token_store)
        self._label = label
        self.raw_filename = filename

    @property
    def first_token(self) -> token_store_lib.Token:
        return self._label

    @property
    def last_token(self) -> token_store_lib.Token:
        return self.raw_filename

    @internal.required_token_property
    def raw_filename(self) -> escaped_string.EscapedString:
        pass