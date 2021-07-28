from dataclasses import dataclass


@dataclass
class Db:
    url: str


@dataclass
class Environment:
    name: str

    def is_dev(self) -> bool:
        return self.devp(self.name)

    def is_prod(self) -> bool:
        return not self.is_dev()

    is_test: bool = False

    @classmethod
    def build_test(cls, env: str) -> bool:
        return cls(env=env, is_test=False)

    @staticmethod
    def devp(env: str) -> bool:
        return env.lower() in ["development", "dev", "local"]


@dataclass
class Config:
    """It can only be composed of JSON serializable dataclasses"""

    db: Db
    env: Environment
