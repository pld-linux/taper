Summary:	A menu-driven file backup system
Summary(de.UTF-8):	Menügesteuertes Backupsystem mit Unterstützung für Komprimierung
Summary(fr.UTF-8):	Système de sauvegarde par menus avec gestion de la compression
Summary(pl.UTF-8):	System do backupów obsługiwany z menu
Summary(tr.UTF-8):	Sıkıştırma desteği sunan, menü tabanlı yedekleme sistemi
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

%description -l de.UTF-8
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

%description -l fr.UTF-8
Programme de sauvegarde et de restauration sur bandes offrant une
interface utilisateur agréable. Les fichiers peuvent aussi être
sauvegardés dans des fichiers sur disque. La sélection des fichiers à
sauvegarder er restaurer est très similaire à l'interface de Midnight
Commander et permet un parcours facile des répertoires. La sélection
récursive des répertoires est possible. La sauvegarde incrémentale et
la restauration automatique de la plus récente sont les valeurs par
défaut. Les lecteurs amovibles, SCSI, ftape, zftape sont reconnus.

%description -l pl.UTF-8
Taper jest programem do obsługi kopii zapasowych z przyjaznym
interfejsem użytkownika. Pliki mogą być składowane na napędzie
taśmowym lub na dysku twardym. Interfejs do wyboru plików jest bardzo
podobny do Midnight Commandera i pozwala na łatwe poruszanie się po
katalogach. Taper daje możliwość rekursywnego wyboru katalogów,
składowanie na SCSI, ftape, zftape oraz dyskach przenośnych.

%description -l tr.UTF-8
Bu yazılım, sevimli bir kullanıcı arayüzüne sahip bir manyetik bant
yedekleme ve geri yükleme sistemidir. Midnight Commander yazılımının
arayüzüne oldukça benzeyen arayüzü sayesinde, dizinleri gezerek
yedeklenecek ya da geri yüklenecek dosyaları seçmek oldukça kolaydır.
SCSI, ftape, zftape ve takılır/çıkarılır sürücüler desteklenmektedir.

%prep
%setup -q -n %{name}-%{version}pre-1
%patch -P0 -p1
%ifarch sparc
%patch -P1 -p1
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
