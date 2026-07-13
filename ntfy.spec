%global debug_package %{nil}

Name: ntfy
Version: 2.25.0
Release: 1%{?dist}
Summary: NTFY build segfault demo
License: ASL 2.0 AND GPLv2
Source0: https://github.com/binwiederhier/ntfy/archive/v%{version}.tar.gz

# using nodejs22-npm shows identical symptoms
BuildRequires: make nodejs24-npm

%description
NTFY build segfault demo.

%prep
%autosetup

%build
# allow core dump
ulimit -c unlimited

# this eventually calls `vite build`
make web
