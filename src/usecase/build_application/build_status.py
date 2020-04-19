from enum import Enum


class BuildStatus(Enum):
    SUCCESSFUL = 0
    FAILED = 1
    FAILED_WITH_CONCURRENT_EXCEPTION = 2
    FAILED_WITH_MONTHLY_LIMIT_EXCEEDED = 3
