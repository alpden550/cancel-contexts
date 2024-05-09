import pytest
from dirty_equals import IsTrueLike, IsFalseLike

from cancel_contexts import CancelContext
from cancel_contexts.exceptions import ContextCancelledError


class TestCancelContext:
    @pytest.fixture
    def ctx(self):
        return CancelContext()

    def test_check_ctx_exception(self, ctx):
        ctx.cancel()
        with pytest.raises(ctx.exception) as exc_info:
            ctx.check_cancelled()

        assert exc_info.type is ContextCancelledError

    def test_cancel_context(self, ctx):
        ctx.cancel()
        assert ctx.cancelled == IsTrueLike

    def test_bool_cancelled_context(self, ctx):
        ctx.cancel()
        assert bool(ctx) == IsFalseLike

    def test_already_cancelled(self, ctx):
        ctx.cancel()
        with pytest.raises(ctx.exception):
            ctx.cancel()
