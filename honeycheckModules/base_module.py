from config import config


class HoneyModule:


    def __init__(self, iface, prefix, config_requirements):
        self.iface = iface
        self.config_requirements = [prefix + '_' + requirement for requirement in config_requirements]


    def check_requirements(self):
        for requirement in self.config_requirements:

            if requirement not in config[self.iface]:
                    return False

        return True

    def check_dependencies(self):
        return True


    def get_req(self, requirement):
        return config[self.iface][requirement]


