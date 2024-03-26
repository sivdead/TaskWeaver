from typing import Literal, Optional

from taskweaver.ces.common import Manager
from taskweaver.ces.environment import Environment, EnvMode
from taskweaver.ces.manager.sub_proc import SubProcessManager


def code_execution_service_factory(
    env_dir: str,
    kernel_mode: Literal["local", "container"] = "local",
    container_network: Optional[str] = None,
) -> Manager:
    return SubProcessManager(
        env_dir=env_dir,
        kernel_mode=kernel_mode,
        container_network=container_network,
    )
