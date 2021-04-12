import os
import platform
import yaml


class Tools:
    def __init__(self, cookies=None):
        self.cookies = cookies

    @staticmethod
    def get_file_dir(file):
        o_path = os.getcwd()
        separator = '\\' if 'Windows' in platform.system() else '/'
        str = o_path
        str = str.split(separator)
        while len(str) > 0:
            spath = separator.join(str) + separator + file
            leng = len(str)
            if os.path.exists(spath):
                return os.path.dirname(spath)
            str.remove(str[leng - 1])

    @staticmethod
    def get_root_dir():
        return Tools.get_file_dir('conftest.py')

    @staticmethod
    def set_env(key, value):
        os.environ[key] = str(value)

    @staticmethod
    def get_env(key=None):
        tmp_system_env = {}
        for tmp_key in os.environ:
            tmp_value = os.environ[tmp_key]
            if tmp_value == "True":
                tmp_value = True
            elif tmp_value == "False":
                tmp_value = False
            tmp_system_env[tmp_key] = tmp_value
        if key:
            return tmp_system_env.get(key)
        return tmp_system_env

    @staticmethod
    def get_config(key=None):
        env = Tools.get_env("TEST_ENV") if Tools.get_env("TEST_ENV") else 'dev'
        with open(os.path.join(Tools.get_root_dir(), 'config', f"{env}.yaml"), encoding="UTF-8") as f:
            config = yaml.load(f.read(), Loader=yaml.SafeLoader)
            if key is not None:
                return config[key]
            return config
