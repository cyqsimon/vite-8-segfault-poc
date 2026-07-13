# vite-8-segfault-poc

This is a POC of a segfault in vite 8.

Original discovery: [COPR: cyqsimon/ntfysh](https://copr.fedorainfracloud.org/coprs/cyqsimon/ntfysh/build/10649601/)

You need a Fedora 44 (tested x86_64 and aarch64) system with internet access.

Check out various branches to test different variations.

## Steps to reproduce

1. Install build tools: `sudo dnf install -y spectool fedpkg`
2. Fetch build source: `spectool --get-files ntfy.spec`
3. Build: `fedpkg --release f44 srpm && fedpkg --release f44 mockbuild --enable-network`
4. Wait and observe the segfault (exit status 139)

## Obtaining a core dump

1. Make sure in `/etc/systemd/coredump.conf`:
   1. `Coredump.Storage` is set to `external`
   2. `Coredump.ExternalSizeMax` is large enough (default `32G`; at least `4G`)
   3. Reboot if you made configuration changes (there may be a better way)
2. Make sure "root" processes in rootless namespace can be dumped: `sudo sysctl -w fs.suid_dumpable=2`
3. Don't let SELinux interfere with `systemd-coredump`: `sudo setenforce 0`
4. After observing segfault, core dump should be available via `coredumpctl`
