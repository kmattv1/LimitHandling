import asyncio
import logging

from src.usecase.build_application.build_status import BuildStatus


class BuildHandler:
    def __init__(self,
                 plan):
        self.plan = plan
        self.active_builds = []
        self.executed_builds_in_this_month = 0

    def add_build_to_the_job_queue(self, build):
        if self.plan.maximum_builds_per_month > self.executed_builds_in_this_month:
            if self.plan.allowed_concurrent_builds > len(self.active_builds):
                return self.__start_build(build)
            else:
                return BuildStatus.FAILED_WITH_CONCURRENT_EXCEPTION
        else:
            return BuildStatus.FAILED_WITH_MONTHLY_LIMIT_EXCEEDED

    def __start_build(self, build):
        self.active_builds.append(build.app_name)
        loop = asyncio.get_event_loop()
        try:
            status = loop.run_until_complete(build.run())
        except Exception as e:
            logging.error(e)
            loop.stop()
            status = BuildStatus.FAILED
        self.executed_builds_in_this_month += 1
        self.active_builds.remove(build.app_name)
        return status
