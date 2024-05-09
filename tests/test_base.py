import pytest
from dirty_equals import IsTrueLike, IsFalseLike

from cancel_contexts.contexts.base import BaseContext


class TestBaseContext:
    @pytest.fixture
    def ctx(self):
        return BaseContext()

    def test_new_context_is_not_cancelled(self, ctx):
        assert ctx.cancelled == IsFalseLike

    def test_bool_new_context_is_not_cancelled(self, ctx):
        assert bool(ctx) == IsTrueLike

    def test_check_ctx_manager(self, ctx):
        with ctx:
            assert ctx.cancelled == IsFalseLike
        assert ctx.cancelled == IsTrueLike
