Summary:	A menu-driven file backup system
Summary(pl):	System do backupów obs³ugiwany z menu
Name:		taper
Version:	6.9
Release:	6
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.e-survey.net.au/%{name}-%{version}.tar.gz
URL:		http://www.e-survey.net.au/taper/
Patch0:		%{name}-%{version}-rh.patch
Patch1:		%{name}-%{version}-sparc.patch
Patch2:		%{name}-%{version}-fix.patch
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

%description -l pl
Taper jest programem do obs³ugi backup'u z przyjaznym interfejsem
u¿ytkownika. Pliki mog± byæ sk³adowane na napêdzie ta¶mowym lub na
dysku twardym. Interfejs do wyboru plików jest bardzo podobny do
Midnight Commander'a i pozwala na ³atwe poruszanie siê po katalogach.
Taper daje mo¿liwo¶æ rekursywnego wyboru katalogów, sk³adowanie na
SCSI, ftape, zftape oraz dyskach przeno¶nych.

%prep
%setup -q
%patch0 -p1 -b .rh

%ifarch sparc
%patch1 -p1 -b .sparc
%endif

%patch2 -p1

find . -name CVS -type d | xargs rm -rf

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
#%{_bindir}/*
%{_mandir}/man8/*
%doc docs/*
