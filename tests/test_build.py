import asyncio
from unittest import TestCase

from src.usecase.build_application.build import Build
from src.usecase.build_application.build_status import BuildStatus


class TestBuild(TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def tearDown(self):
        self.loop.close()

    def test_given_new_build_is_created_when_build_is_executed_then_status_is_success(self):
        # Given
        build = Build("test")

        # When
        status = self.loop.run_until_complete(build.run())

        # Then
        assert status == BuildStatus.SUCCESSFUL

    def test_when_app_name_is_defined_then_it_is_succesfully_set(self):
        # When
        build = Build("test")

        # Then
        assert build.get_app_name() == "test"
