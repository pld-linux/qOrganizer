# TODO:
# - optflags
# - WARNING! For me this app on secondary run eats all memory
#   (when it reads configuration/stored data) 
Summary:	General organizer
Summary(pl.UTF-8):	Ogólny organizer
Name:		qOrganizer
Version:	3.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qorganizer/%{name}-v%{version}.tar.gz
# Source0-md5:	a562ea6baecaedb08cd6c126cab523eb
Source1:	%{name}.desktop
URL:		http://qorganizer.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-linguist >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qOrganizer is a general organizer that includes calendar with journal
and schedule for every day in which you can choose to be reminded of
events, a general to-do list for your tasks and also includes features
useful for students like timetable and a booklet with marks and
absences.

%description -l pl.UTF-8
qOrganizer to ogólny organizer zawierający kalendarz z dziennikiem i
planem na każdy dzień, z którego można wybierać zdarzenia do
przypomnienia, ogólną listą zadań do wykonania oraz elementami
przydatnymi dla uczniów i studentów, takimi jak plan zajęć czy
notatnik z ocenami i nieobecnościami.

%prep
%setup -q -n %{name}
# remove binary files
rm -f src/%{name} src/lang/*.qm

%build
cd src
lrelease-qt4 lang/*.ts
qmake-qt4 %{name}.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
