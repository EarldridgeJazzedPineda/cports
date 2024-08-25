pkgname = "cjs"
pkgver = "128.0"
pkgrel = 0
build_style = "meson"
# Profiler does not build on musl libc, see https://bugs.gentoo.org/937390
configure_args = [
    "--libexecdir=/usr/lib",  # XXX: drop libexec
    "-Dinstalled_tests=false",
    "-Dprofiler=disabled",
    "-Dskip_gtk_tests=true",
]
hostmakedepends = [
    "dbus",
    "gobject-introspection",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk4-devel",
    "libffi8-devel",
    "mozjs128-devel",
    "readline-devel",
]
pkgdesc = "Cinnamon JavaScript interpreter"
license = "MIT OR LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cjs/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d3432dd2722eef65b4a36db430824882b3bd90b4db469f576ff087d045e022ca"
patch_style = "patch"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/lib/installed-tests")


@subpackage("cjs-devel")
def _(self):
    return self.default_devel()
