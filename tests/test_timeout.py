import pytest
from time import sleep


class TestTimeOutContext:
    SLEEP_TIME = 0.5

    @pytest.fixture
    def context(self):
        from cancel_contexts.contexts.timeout import TimeOutContext

        return TimeOutContext(self.SLEEP_TIME)

    def test_timeout(self, context):
        sleep(self.SLEEP_TIME + 0.1)
        assert context.is_timer_finished

    def test_cancel(self, context):
        context.cancel()
        assert context.cancelled

    def test_check_cancelled(self, context):
        context.cancel()
        with pytest.raises(context.exception):
            context.check_cancelled()

    def test_bool_timed_out_context(self, context):
        sleep(self.SLEEP_TIME + 0.1)
        assert bool(context) is False
