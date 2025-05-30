pkgname = "dtach"
pkgver = "0.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Program that emulates the detach feature of screen"
license = "GPL-2.0-or-later"
url = "https://dtach.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/dtach/dtach-{pkgver}.tar.gz"
sha256 = "32e9fd6923c553c443fab4ec9c1f95d83fa47b771e6e1dafb018c567291492f3"
# Makefile has no check target
options = ["!check"]


def install(self):
    self.install_bin("build/dtach")
    self.install_man("dtach.1")
