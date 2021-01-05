# -*- coding: utf-8 -*-
import os

import docker
from docker.client import DockerClient


def main(client: DockerClient) -> None:
    """
    Create wheels for all manylinux platforms.
    """
    print("""=========================================================""")
    print("""           Building Manylinux aarch64 Wheels             """)
    print("""=========================================================""")
    client.containers.run(
        "quay.io/pypa/manylinux2014_aarch64",
        "/io/scripts/manylinux.sh",
        platform="linux/arm64",
        volumes={os.getcwd(): {"bind": "/io"}},
    )
    print("""=========================================================""")
    print("""           Building Manylinux x86_64 Wheels              """)
    print("""=========================================================""")
    client.containers.run(
        "quay.io/pypa/manylinux2014_x86_64",
        "/io/scripts/manylinux.sh",
        volumes={os.getcwd(): {"bind": "/io"}},
    )

    print("""=========================================================""")
    print("""            Building Manylinux i686 Wheels               """)
    print("""=========================================================""")
    client.containers.run(
        "quay.io/pypa/manylinux2014_i686",
        "/io/scripts/manylinux.sh",
        volumes={os.getcwd(): {"bind": "/io"}},
    )
    print("Wheels built Successfully.")


if __name__ == "__main__":
    main(docker.from_env())
