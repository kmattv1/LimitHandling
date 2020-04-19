class Plan:
    def __init__(self,
                 name,
                 allowed_concurrent_builds,
                 build_time_limits_in_minutes,
                 maximum_builds_per_month,
                 maximum_number_of_team_members,
                 maximum_number_of_apps):
        self.name = name
        self.allowed_concurrent_builds = allowed_concurrent_builds
        self.build_time_limits_in_minutes = build_time_limits_in_minutes
        self.maximum_builds_per_month = maximum_builds_per_month
        self.maximum_number_of_team_members = maximum_number_of_team_members
        self.maximum_number_of_apps = maximum_number_of_apps

    def get_name(self):
        return self.name

    def get_number_of_allowed_concurrent_builds(self):
        return self.allowed_concurrent_builds

    def get_build_time_limits_in_minutes(self):
        return self.build_time_limits_in_minutes

    def get_number_of_maximum_builds_pre_month(self):
        return self.maximum_builds_per_month

    def get_number_of_maximum_team_members(self):
        return self.maximum_number_of_team_members

    def get_number_of_allowed_apps_in_the_plan(self):
        return self.maximum_number_of_apps


class Free(Plan):
    def __init__(self):
        self.name = "Free"
        self.allowed_concurrent_builds = 1
        self.build_time_limits_in_minutes = 10
        self.maximum_builds_per_month = 200
        self.maximum_number_of_team_members = 2
        self.maximum_number_of_apps = None


class Developer(Plan):
    def __init__(self):
        self.name = "Developer"
        self.allowed_concurrent_builds = 2
        self.build_time_limits_in_minutes = 45
        self.maximum_builds_per_month = None
        self.maximum_number_of_team_members = None
        self.maximum_number_of_apps = None


class Organization(Plan):
    def __init__(self):
        self.name = "Organization"
        self.allowed_concurrent_builds = 4
        self.build_time_limits_in_minutes = 90
        self.maximum_builds_per_month = None
        self.maximum_number_of_team_members = None
        self.maximum_number_of_apps = None


class Public(Plan):
    def __init__(self):
        self.name = "Public"
        self.allowed_concurrent_builds = 2
        self.build_time_limits_in_minutes = 45
        self.maximum_builds_per_month = None
        self.maximum_number_of_team_members = None
        self.maximum_number_of_apps = 1
