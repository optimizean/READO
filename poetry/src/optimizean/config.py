import os
import sys
from importlib.metadata import metadata  # >= 3.8
from dataclasses import dataclass, field, fields


def get_metadata(package_name="optimizean"):
    meta = metadata(package_name)
    return meta


meta = get_metadata()


@dataclass
class UserConfig:
    user_os: str = os.uname().sysname
    python_major_version: int = sys.version_info.major
    python_minor_version: int = sys.version_info.minor


@dataclass
class ProjectConfig:
    name: str = meta["name"]
    version: str = meta["version"]
    # description: str = meta["description"]
    # authors: list = meta["authors"]
    license: str = meta["license"]


@dataclass
class StyleConfig:
    main: str = "green3"
    sub: str = "dark_slate_gray1"
    emp: str = "magenta"


@dataclass
class Parameters:
    user: UserConfig = field(default_factory=UserConfig)
    setup: ProjectConfig = field(default_factory=ProjectConfig)
    style: StyleConfig = field(default_factory=StyleConfig)

    def to_dict(self):
        return self.__dict__

    def __repr__(self) -> str:
        field_strs = (f"{f.name}={getattr(self, f.name)!r}" for f in fields(self))
        # return f"Parameters({','.join(field_strs)})"
        return "\nParameters(" + ",\n\t".join(field_strs) + ")"


def main():
    params = Parameters()
    return params


if __name__ == "__main__":
    params = main()
    # print(params.__repr__)
