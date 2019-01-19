# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestDashlane::test_file 1'] = 'example login (example.com: user@example.com)'

snapshots['TestDashlane::test_file 2'] = 'p455w0rd'

snapshots['TestDashlane::test_file 3'] = 'second example (example.com: example)'

snapshots['TestDashlane::test_file 4'] = 'g00dp455'
