Summary: A menu-driven file backup system.
Name: taper
Version: 6.9
Release: 6
Copyright: GPL
Group: Applications/Archiving
Source: http://www.omen.com.au/~yusuf/taper-%{version}.tar.gz
URL: http://www.omen.com.au/~yusuf
Patch0: taper-%{version}-rh.patch
Patch1: taper-%{version}-sparc.patch
Patch2: taper-%{version}-fix.patch
Buildroot: /var/tmp/taper-root

%description
Taper is a backup and restoration program with a friendly user
interface.  Files may be backed up to a tape drive or to a hard disk.
The interface for selecting files to be backed up/restored is very
similar to the Midnight Commander interface, and allows easy traversal
of directories.  Taper supports recursive selection of directories.
Taper also supports backing up SCSI, ftape, zftape and removable drives.
By default, taper is set for incremental backups and automatic most
recent restore.

Install the taper package if you need a user friendly file backup and
restoration program.

%prep
%setup -q
%patch0 -p1 -b .rh

%ifarch sparc
%patch1 -p1 -b .sparc
%endif

%patch2 -p1

find . -name CVS -type d | xargs rm -rf

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/*
#/usr/bin/*
%doc docs/*
