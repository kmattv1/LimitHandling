from tornado_swagger.model import register_swagger_model


@register_swagger_model
class ApplicationLimits:
    """
    ---
    type: object
    description: Limits response model representation
    properties:
        applicationName:
            type: string
        plan:
            type: string
        allowedConcurrentBuilds:
            type: integer
            format: int64
        buildTimeLimitInMinutes:
            type: integer
            format: int64
        maximumBuildsPerMonth:
            type: integer
            format: int64
        isPublic:
            type: boolean
            default: false
    """

    @staticmethod
    def get_limits_dict(application, plan):
        return {
            "applicationName": application.get_name(),
            "plan": plan.get_name(),
            "allowedConcurrentBuilds": plan.get_number_of_allowed_concurrent_builds(),
            "buildTimeLimitInMinutes": plan.get_build_time_limits_in_minutes(),
            "maximumBuildsPerMonth": plan.get_number_of_maximum_builds_pre_month(),
            "isPublic": application.get_is_public()
        }
