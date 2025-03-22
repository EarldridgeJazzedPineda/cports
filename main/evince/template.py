pkgname = "evince"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
# dvi needs kpathsea, which is in texlive
# does anyone actually need dvi?
configure_args = [
    "-Dintrospection=true",
    "-Dgtk_doc=false",
    "-Dnautilus=false",
    "-Dcomics=enabled",
    "-Dps=enabled",
    "-Ddvi=disabled",
    "-Dsystemduserunitdir=no",
]
hostmakedepends = [
    "adwaita-icon-theme",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "itstool",
    "meson",
    "perl-xml-parser",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "djvulibre-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "gspell-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libarchive-devel",
    "libgxps-devel",
    "libhandy-devel",  # "nautilus-devel",
    "libsecret-devel",
    "libspectre-devel",
    "libtiff-devel",
    "poppler-devel",
]
pkgdesc = "GNOME document viewer"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Evince"
source = (
    f"$(GNOME_SITE)/evince/{pkgver[: pkgver.find('.')]}/evince-{pkgver}.tar.xz"
)
sha256 = "cd2f658355fa9075fdf9e5b44aa0af3a7e0928c55614eb1042b36176cf451126"


@subpackage("evince-libs")
def _(self):
    return self.default_libs()


@subpackage("evince-devel")
def _(self):
    return self.default_devel()
