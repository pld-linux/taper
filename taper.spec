Summary:	A menu-driven file backup system
Name:		taper
Version:	6.9
Release:	6
License:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source0:	http://www.omen.com.au/~yusuf/%{name}-%{version}.tar.gz
URL:		http://www.omen.com.au/~yusuf
Patch0:		taper-%{version}-rh.patch
Patch1:		taper-%{version}-sparc.patch
Patch2:		taper-%{version}-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Taper is a backup and restoration program with a friendly user
interface. Files may be backed up to a tape drive or to a hard disk.
The interface for selecting files to be backed up/restored is very
similar to the Midnight Commander interface, and allows easy traversal
of directories. Taper supports recursive selection of directories.
Taper also supports backing up SCSI, ftape, zftape and removable
drives. By default, taper is set for incremental backups and automatic
most recent restore.

%prep
%setup -q
%patch0 -p1 -b .rh

%ifarch sparc
%patch1 -p1 -b .sparc
%endif

%patch2 -p1

find . -name CVS -type d | xargs rm -rf

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
#%{_bindir}/*
%doc docs/*
