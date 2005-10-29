Summary:	A menu-driven file backup system
Summary(de):	Menügesteuertes Backupsystem mit Unterstützung für Komprimierung
Summary(fr):	Système de sauvegarde par menus avec gestion de la compression
Summary(pl):	System do backupów obs³ugiwany z menu
Summary(tr):	Sýkýþtýrma desteði sunan, menü tabanlý yedekleme sistemi
Name:		taper
Version:	7.0
%define		_pre	pre1
Release:	0.%{_pre}.1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/taper/%{name}-%{version}pre-1.tar.gz
# Source0-md5:	d8e983c3ba24af2feb03290e66e43a93
URL:		http://taper.sourceforge.net/
Patch0:		%{name}-%{version}-rh.patch
Patch1:		%{name}-%{version}-sparc.patch
BuildRequires:	ncurses-ext-devel
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

%description -l de
Ein Band-Backup- und Wiederherstellungsprogramm mit einer freundlichen
Bedienungsoberfläche zum Sichern/Wiederherstellen von Dateien in
Kombination mit einem Bandlaufwerk. Alternativ können Dateien auch auf
Festplatte gespeichert werden. Die Auswahl der zu sichernden bzw.
wiederherzustellenden Dateien ist ähnlich wie beim Midight Commander -
mit einfachem Verzeichniswechsel. Rekursiv ausgewählte Verzeichnisse
werden unterstützt; inkrementelle Backups und automatische
Wiederherstellung der zuletzt gespeicherten Version sind
Standardeinstellungen. SCSI, ftape, zftape und Wechselplatten werden
unterstützt.

%description -l fr
Programme de sauvegarde et de restauration sur bandes offrant une
interface utilisateur agréable. Les fichiers peuvent aussi être
sauvegardés dans des fichiers sur disque. La sélection des fichiers à
sauvegarder er restaurer est très similaire à l'interface de Midnight
Commander et permet un parcours facile des répertoires. La sélection
récursive des répertoires est possible. La sauvegarde incrémentale et
la restauration automatique de la plus récente sont les valeurs par
défaut. Les lecteurs amovibles, SCSI, ftape, zftape sont reconnus.

%description -l pl
Taper jest programem do obs³ugi kopii zapasowych z przyjaznym
interfejsem u¿ytkownika. Pliki mog± byæ sk³adowane na napêdzie
ta¶mowym lub na dysku twardym. Interfejs do wyboru plików jest bardzo
podobny do Midnight Commandera i pozwala na ³atwe poruszanie siê po
katalogach. Taper daje mo¿liwo¶æ rekursywnego wyboru katalogów,
sk³adowanie na SCSI, ftape, zftape oraz dyskach przeno¶nych.

%description -l tr
Bu yazýlým, sevimli bir kullanýcý arayüzüne sahip bir manyetik bant
yedekleme ve geri yükleme sistemidir. Midnight Commander yazýlýmýnýn
arayüzüne oldukça benzeyen arayüzü sayesinde, dizinleri gezerek
yedeklenecek ya da geri yüklenecek dosyalarý seçmek oldukça kolaydýr.
SCSI, ftape, zftape ve takýlýr/çýkarýlýr sürücüler desteklenmektedir.

%prep
%setup -q -n %{name}-%{version}pre-1
%patch0 -p1
%ifarch sparc
%patch1 -p1
%endif

find . -name CVS -type d | xargs rm -rf

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
