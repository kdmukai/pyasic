# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.miners.backends import Hiveon
from pyasic.miners.device.models import (
    S19,
    S19L,
    S19XP,
    S19a,
    S19aPro,
    S19Hydro,
    S19i,
    S19j,
    S19jNoPIC,
    S19jPro,
    S19KPro,
    S19Plus,
    S19Pro,
    S19ProHydro,
    S19ProPlus,
    S19ProPlusHydro,
)


class HiveonS19(Hiveon, S19):
    pass


class HiveonS19Plus(Hiveon, S19Plus):
    pass


class HiveonS19i(Hiveon, S19i):
    pass


class HiveonS19Pro(Hiveon, S19Pro):
    pass


class HiveonS19ProPlus(Hiveon, S19ProPlus):
    pass


class HiveonS19XP(Hiveon, S19XP):
    pass


class HiveonS19a(Hiveon, S19a):
    pass


class HiveonS19aPro(Hiveon, S19aPro):
    pass


class HiveonS19j(Hiveon, S19j):
    pass


class HiveonS19jNoPIC(Hiveon, S19jNoPIC):
    pass


class HiveonS19jPro(Hiveon, S19jPro):
    pass


class HiveonS19L(Hiveon, S19L):
    pass


class HiveonS19ProHydro(Hiveon, S19ProHydro):
    pass


class HiveonS19Hydro(Hiveon, S19Hydro):
    pass


class HiveonS19ProPlusHydro(Hiveon, S19ProPlusHydro):
    pass


class HiveonS19KPro(Hiveon, S19KPro):
    pass
