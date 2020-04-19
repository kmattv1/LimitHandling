class ListLimitsOfAnApplication:
    def __init__(self, application_repository):
        self.application_repository = application_repository

    def get_limits(self, application_name):
        application = self.application_repository.get_application(application_name)
        plan = application.get_plan()
        limits = {
            "ApplicationName": application.get_app_name(),
            "Plan": plan.get_name(),
            "AllowedConcurrentBuilds": plan.get_number_of_allowed_concurrent_builds(),
            "BuildTimeLimitInMinutes": plan.get_build_time_limits_in_minutes(),
            "MaximumBuildsPerMonth": plan.get_number_of_maximum_builds_pre_month(),
            "IsPublic": application.get_is_public()
        }
        return limits
