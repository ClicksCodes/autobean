from lark import exceptions
import pytest
from autobean.refactor.models import raw_models
from . import base


class TestWhitespace(base.BaseTestModel):

    @pytest.mark.parametrize(
        'text', [
            ' ',
            '    ',
            '\t',
            '\t\t\t\t',
            ' \t \t',
        ],
    )
    def test_parse_success(self, text: str) -> None:
        token = self.raw_parser.parse_token(text, raw_models.Whitespace)
        assert token.raw_text == text
        self.check_deepcopy_token(token)

    @pytest.mark.parametrize(
        'text', [
            ''
            '\n',
            '\u00a0',
            '\u2000',
        ],
    )
    def test_parse_failure(self, text: str) -> None:
        with pytest.raises(exceptions.UnexpectedInput):
            self.raw_parser.parse_token(text, raw_models.Whitespace)
