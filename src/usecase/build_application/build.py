import asyncio
import logging

from src.usecase.build_application.build_status import BuildStatus


class Build:
    def __init__(self, app_name):
        self.app_name = app_name

    def get_app_name(self):
        return self.app_name

    async def run(self):
        logging.info("Started building application: " + self.app_name)
        await asyncio.sleep(2)
        return BuildStatus.SUCCESSFUL
