pkgname = "flatpak-kcm"
pkgver = "6.3.3"
pkgrel = 0
build_style = "cmake"
# segfaults in libflatpak probably due to checking system-repo related stuff
# in chroot
make_check_args = ["-E", "flatpakpermissiontest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "flatpak-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE Flatpak permissions KCM"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/flatpak-kcm"
source = f"$(KDE_SITE)/plasma/{pkgver}/flatpak-kcm-{pkgver}.tar.xz"
sha256 = "7d5a9328738a4e8cf339417baa63f2b941b5147e50d60d9f11cf40d3ec9da695"
hardening = ["vis"]
