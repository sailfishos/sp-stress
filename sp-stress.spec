Name: sp-stress
Version: 0.2.0
Release: 1%{?dist}
Summary: Tools for creating stress test loads
Group: Development/Tools
License: GPLv2+
URL: https://github.com/mer-tools/sp-stress
Source: %{name}-%{version}.tar.gz

%description
   Contains the following tools:
   - `swpload' exercises the kernel virtual memory subsystem by creating
     clients that access memory pages with configurable patterns.
   - `cpuload' generates CPU load according to specified value.
   - `memload' allocates configurable amount of memory.
   - `flash_eater' allocates disk space on the filesystem so that only a
     configurable amount of free space will be left.
   - `run_secs' allows execution of given command for a configurable time
     period, after which it will be terminated.

%prep
# Adjusting %%setup since git-pkg unpacks to src/
# %%setup -q
%setup -q -n src

%build
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/ioload
%{_bindir}/swpload
%{_bindir}/memload
%{_bindir}/cpuload
%{_bindir}/run_secs
%{_bindir}/flash_eater
%{_mandir}/man1/*.1.gz
%doc doc/README COPYING 
