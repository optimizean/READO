import os
import sys
from importlib.metadata import (
    metadata,
    version,
    requires,
)  # >= 3.8
from dataclasses import dataclass, field, fields


# -- Load Metadata -- #
def get_metadata(package_name="optimizean"):
    meta = metadata(package_name)
    return meta


meta = get_metadata()

# -- Metadata Dataclass -- #


@dataclass
class UserConfig:
    user_os: str = os.uname().sysname
    python_major_version: int = sys.version_info.major
    python_minor_version: int = sys.version_info.minor


@dataclass
class ProjectConfig:
    name: str = meta.get("name", "unknown")
    version: str = meta.get("version", version("optimizean"))
    license: str = meta.get("license", "unknown")
    dependencies: list = field(default_factory=lambda: requires("optimizean"))


@dataclass
class StyleConfig:
    main: str = "green3"
    sub: str = "dark_slate_gray1"
    emp: str = "magenta"


class AuthorConfig:
    name: str = "optimizean"
    github: str = "https://github.com/optimizean"
    blog: str = "https://optimizean.github.io/an/"
    email: str = "optimize.an@gmail.com"


@dataclass
class Parameters:
    user: UserConfig = field(default_factory=UserConfig)
    project: ProjectConfig = field(default_factory=ProjectConfig)
    style: StyleConfig = field(default_factory=StyleConfig)
    author: AuthorConfig = field(default_factory=AuthorConfig)

    def to_dict(self):
        return self.__dict__

    def __repr__(self) -> str:
        field_strs = (f"{f.name}={getattr(self, f.name)!r}" for f in fields(self))
        # return f"Parameters({','.join(field_strs)})"
        return "\nParameters(" + ",\n\t".join(field_strs) + ")"


def main():
    config = Parameters()
    return config


if __name__ == "__main__":
    config = main()
    print(config.__repr__)
