pkgname = "localsearch"
pkgver = "3.8.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddefault_library=shared",
    "-Dextract=true",
    "-Dfunctional_tests=false",
    "-Dman=true",
    "-Dsystemd_user_services=false",
    # features
    "-Dminer_rss=false",  # libgrss hasn't been touched in a while
    "-Dplaylist=enabled",
    "-Dlandlock=enabled",
    "-Dexif=enabled",
    "-Djpeg=enabled",
    "-Dtiff=enabled",
    "-Diptc=enabled",
    "-Draw=enabled",
    "-Dxps=enabled",
    "-Dpng=enabled",
    "-Dgif=enabled",
    "-Dpdf=enabled",
    "-Dxml=enabled",
    "-Dcue=enabled",
    "-Dgsf=enabled",
    "-Diso=enabled",
]
hostmakedepends = [
    "asciidoc",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "tinysparql-devel",
    "glib-devel",
    "dbus-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "icu-devel",
    "libexif-devel",
    "libseccomp-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "giflib-devel",
    "libxml2-devel",
    "poppler-devel",
    "upower-devel",
    "exempi-devel",
    "networkmanager-devel",
    "gexiv2-devel",
    "totem-pl-parser-devel",
    "libgxps-devel",
    "libcue-devel",
    "libgsf-devel",
    "libiptcdata-devel",
    "libosinfo-devel",
]
provides = [self.with_pkgver("tracker-miners")]
pkgdesc = "Data miners for tinysparql"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tinysparql"
source = f"$(GNOME_SITE)/localsearch/{pkgver[:-2]}/localsearch-{pkgver}.tar.xz"
sha256 = "a7b24a4f07805df7543a4dd023684fcde5ee699ca00eb5b09123a049d3aeccd8"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# check relies on stuff unsupported in chroot
options = ["!check", "!cross"]
