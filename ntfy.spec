%global debug_package %{nil}

Name: ntfy
Version: {{{ git_dir_version }}}
Release: 1%{?dist}
Summary: NTFY build segfault demo
License: ASL 2.0 AND GPLv2
VCS: {{{ git_dir_vcs }}}
Source0: {{{ git_dir_pack }}}

# using nodejs22-npm shows identical symptoms
BuildRequires: make nodejs24-npm

%description
NTFY build segfault demo.

%prep
{{{ git_dir_setup_macro }}}

%build
# allow core dump
ulimit -c unlimited

# this eventually calls `vite build`
make web
