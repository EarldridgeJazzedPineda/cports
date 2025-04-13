pkgname = "incus"
pkgver = "6.9.0"
pkgrel = 3
build_style = "go"
make_build_args = ["./cmd/..."]
make_check_args = ["-skip", "TestConvertNetworkConfig", "./..."]
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "acl-devel",
    "cowsql-devel",
    "libatomic-chimera-devel-static",
    "libseccomp-devel",
    "libcap-devel",
    "linux-headers",
    "libuv-devel",
    "libunwind-devel-static",
    "lxc-devel",
    "musl-devel-static",
    "raft-devel",
    "sqlite-devel",
    "udev-devel",
]
depends = [
    "acl-progs",
    "attr-progs",
    "dnsmasq",
    "gtar",
    "iptables",
    "libvirt",
    "lxc",
    "rsync",
    "squashfs-tools",
    "util-linux",
    "xz",
    self.with_pkgver("incus-client"),
]
go_build_tags = ["libsqlite3"]
go_check_tags = ["libsqlite3"]
pkgdesc = "Powerful system container and virtual machine manager"
license = "Apache-2.0"
url = "https://github.com/lxc/incus"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7c50d4eb2ae5a33eab27821c95e01fc9a5d977c9b6b594a51571e6fefd4119d2"
# fail to link because of post_build overrides
options = ["!check"]


def post_build(self):
    # Build the agent statically
    self.env["CGO_ENABLED"] = "1"
    self.env["CGO_LDFLAGS"] = "-static-pie"
    self.go_build_tags = ["agent", "netgo", "osusergo"]
    self.make_build_args = ["./cmd/incus-agent"]
    self.golang.build()


def post_install(self):
    self.install_service(self.files_path / "incus")
    self.install_service(self.files_path / "incus-user")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_file("^/envfile", "usr/share/incus")


@subpackage("incus-client")
def _(self):
    self.subdesc = "client only"
    self.depends = [self.parent]

    return ["usr/bin/incus"]
