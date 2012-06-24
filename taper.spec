Summary:	A menu-driven file backup system
Summary(de):	Men�gesteuertes Backupsystem mit Unterst�tzung f�r Komprimierung
Summary(fr):	Syst�me de sauvegarde par menus avec gestion de la compression
Summary(pl):	System do backup�w obs�ugiwany z menu
Summary(tr):	S�k��t�rma deste�i sunan, men� tabanl� yedekleme sistemi
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
Bedienungsoberfl�che zum Sichern/Wiederherstellen von Dateien in
Kombination mit einem Bandlaufwerk. Alternativ k�nnen Dateien auch auf
Festplatte gespeichert werden. Die Auswahl der zu sichernden bzw.
wiederherzustellenden Dateien ist �hnlich wie beim Midight Commander -
mit einfachem Verzeichniswechsel. Rekursiv ausgew�hlte Verzeichnisse
werden unterst�tzt; inkrementelle Backups und automatische
Wiederherstellung der zuletzt gespeicherten Version sind
Standardeinstellungen. SCSI, ftape, zftape und Wechselplatten werden
unterst�tzt.

%description -l fr
Programme de sauvegarde et de restauration sur bandes offrant une
interface utilisateur agr�able. Les fichiers peuvent aussi �tre
sauvegard�s dans des fichiers sur disque. La s�lection des fichiers �
sauvegarder er restaurer est tr�s similaire � l'interface de Midnight
Commander et permet un parcours facile des r�pertoires. La s�lection
r�cursive des r�pertoires est possible. La sauvegarde incr�mentale et
la restauration automatique de la plus r�cente sont les valeurs par
d�faut. Les lecteurs amovibles, SCSI, ftape, zftape sont reconnus.

%description -l pl
Taper jest programem do obs�ugi kopii zapasowych z przyjaznym
interfejsem u�ytkownika. Pliki mog� by� sk�adowane na nap�dzie
ta�mowym lub na dysku twardym. Interfejs do wyboru plik�w jest bardzo
podobny do Midnight Commandera i pozwala na �atwe poruszanie si� po
katalogach. Taper daje mo�liwo�� rekursywnego wyboru katalog�w,
sk�adowanie na SCSI, ftape, zftape oraz dyskach przeno�nych.

%description -l tr
Bu yaz�l�m, sevimli bir kullan�c� aray�z�ne sahip bir manyetik bant
yedekleme ve geri y�kleme sistemidir. Midnight Commander yaz�l�m�n�n
aray�z�ne olduk�a benzeyen aray�z� sayesinde, dizinleri gezerek
yedeklenecek ya da geri y�klenecek dosyalar� se�mek olduk�a kolayd�r.
SCSI, ftape, zftape ve tak�l�r/��kar�l�r s�r�c�ler desteklenmektedir.

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
