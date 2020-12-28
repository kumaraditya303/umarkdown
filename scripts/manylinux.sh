#!/bin/bash
mkdir -p /tmp/temp-wheels

find /tmp/temp-wheels/ -type f -delete

for PYBIN in /opt/python/cp3[789]*/bin; do
    "${PYBIN}/pip" install -q -U setuptools wheel --no-cache-dir
    (cd /io/ && "${PYBIN}/python" -m pip install .)
    (cd /io/ && "${PYBIN}/python" setup.py -q bdist_wheel -d /tmp/temp-wheels)
done

"$PYBIN/pip" install -q auditwheel

mkdir -p /io/dist/

for whl in /tmp/temp-wheels/*.whl; do
    auditwheel repair "$whl" -w /io/dist/
done
