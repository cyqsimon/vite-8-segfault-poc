%global debug_package %{nil}

Name: ntfy
Version: 2.25.0
Release: 1%{?dist}
Summary: NTFY build segfault demo
License: ASL 2.0 AND GPLv2
Source0: https://github.com/binwiederhier/ntfy/archive/v%{version}.tar.gz
Source1: https://github.com/rolldown/rolldown/archive/v1.1.2.tar.gz
Patch0: mimalloc-v2.patch

# using nodejs22-npm shows identical symptoms
BuildRequires: cargo cmake curl gcc-c++ git just make nodejs24-npm

%description
NTFY build segfault demo.

%prep
%setup -DTq -b0 -b1

cd ../rolldown-*
%patch -P0 -p1

%build
cd ..
realpath .

# allow core dump
ulimit -c unlimited

# build rolldown
# ====================
pushd rolldown-*
just setup-vite-plus
. "$HOME/.vite-plus/env"
vp install
just build-rolldown-binding
popd

# build ntfy
# ====================
pushd ntfy-*
pushd web
npm ci
popd
# replace rolldown binary
b2sum web/node_modules/@rolldown/binding-*/rolldown-binding.*.node
cp ../rolldown-*/packages/rolldown/src/rolldown-binding.*.node web/node_modules/@rolldown/binding-*/
b2sum web/node_modules/@rolldown/binding-*/rolldown-binding.*.node
# build and run checksum again to make sure the rolldown binary is still our version
if make web-build; then
  b2sum web/node_modules/@rolldown/binding-*/rolldown-binding.*.node
else
  b2sum web/node_modules/@rolldown/binding-*/rolldown-binding.*.node
  exit 1
fi
popd
