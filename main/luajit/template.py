pkgname = "luajit"
pkgver = "2.1_p20250117"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "ppc", "x86_64"]
_tests_rev = "a3a5deb5d97d57fb4da567017a621ae73ee7305e"
build_style = "makefile"
make_build_target = "amalg"
make_build_args = ["PREFIX=/usr", "Q=", "E=@:"]
make_use_env = True
hostmakedepends = ["pkgconf"]
checkdepends = [
    "perl",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "OpenResty's LuaJIT fork"
license = "MIT"
url = "https://github.com/openresty/luajit2"
source = [
    f"{url}/archive/refs/tags/v{pkgver.replace('_p', '-')}.tar.gz",
    f"{url}-test-suite/archive/{_tests_rev}.tar.gz",
]
source_paths = [
    ".",
    "test-suite",
]
sha256 = [
    "68ff3dc2cc97969f7385679da7c9ff96738aa9cc275fa6bab77316eb3340ea8e",
    "b9862f002768dac55c8ab3d1ea21f3aa06d4075f6d022bb2eff76e82df264ffc",
]
hardening = []
# cba
options = ["!cross"]


if self.profile().arch == "aarch64":
    # fails buildvm
    hardening += ["!int"]


def init_build(self):
    cc = self.get_tool("CC")
    cfl = self.get_cflags(shell=True)
    ldfl = self.get_ldflags(shell=True)
    hcc = self.get_tool("CC", target="host")
    hcfl = self.get_cflags(shell=True, target="host")
    hldfl = self.get_ldflags(shell=True, target="host")
    # build system is dumb and does not pass link args properly
    self.make_build_args += [
        f"CC={cc}",
        f"TARGET_CFLAGS={cfl}",
        f"TARGET_LDFLAGS={cfl} {ldfl}",
        f"TARGET_SHLDFLAGS={cfl} {ldfl}",
        f"HOST_CC={hcc}",
        f"HOST_CFLAGS={hcfl}",
        f"HOST_LDFLAGS={hcfl} {hldfl}",
    ]


def check(self):
    pfx = str(self.chroot_cwd / "test-suite/target")
    self.do("make", "install", "PREFIX=" + pfx)
    self.do(
        "./run-tests",
        pfx,
        f"{pfx}/bin/luajit",
        "clang",
        "clang++",
        wrksrc="test-suite",
    )


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("luajit-devel")
def _(self):
    return self.default_devel()
