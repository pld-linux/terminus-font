Summary:	A clean fixed width font
Summary(pl):	Przejrzysty font o sta�ej szeroko�ci
Name:		terminus-font
Version:	4.09
Release:	1
Epoch:		0
License:	GPL
Group:		Fonts
Source0:	http://www.is-vn.bg/hamster/%{name}-%{version}.tar.gz
# Source0-md5:	21e832a4b4bfdd1f494eddea06ccfedf
URL:		http://www.is-vn.bg/hamster/jimmy-en.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminus Font is designed for long (8 and more hours per day) work
with computers. Version 4.09 contains 594 characters, covering code
pages ISO8859-1/2/5/9/13/15/16, Windows-1250/1251/1252/1254/1257,
IBM-437/852/855/866, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian and Esperanto, and also the
vt100 and xterm pseudographic characters.

The sizes present are 8x14, 8x16, 10x20, 12x24, 14x28 and 16x32. The
styles are normal and bold, plus EGA/VGA-bold for 8x14 and 8x16.

%description -l pl
Font Terminus jest zaprojektowany do d�ugiej (8 i wi�cej godzin
dziennie) pracy z komputerami. Wersja 4.09 zawiera 594 znaki,
pokrywaj�ce strony kodowe ISO8859-1/2/5/9/13/15/16,
Windows-1250/1251/1252/1254/1257, IBM-437/852/855/866, KOI8-R/U/E/F,
Bulgarian-MIK,Paratype-PT154/PT254, Macintosh-Ukrainian i Esperanto, a
tak�e znaki pseudograficzne vt100 i xterma.

Dost�pne s� rozmiary 8x14, 8x16, 10x20, 12x24, 14x28 i 16x32. Style to
normalny i pogrubiony, oraz pogrubiony EGA/VGA dla 8x14 i 8x16.

%package console
Summary:	A clean fixed width font
Summary(pl):	Przejrzysty font o sta�ej szeroko�ci
Group:		Fonts

%description console
Terminus Font is designed for long (8 and more hours per day) work
with computers. Version 4.09 contains 594 characters, covering code
pages ISO8859-1/2/5/9/13/15/16, Windows-1250/1251/1252/1254/1257,
IBM-437/852/855/866, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian and Esperanto, and also the
vt100 and xterm pseudographic characters.

The sizes present are 8x14, 8x16, 10x20, 12x24, 14x28 and 16x32. The
styles are normal and bold, plus EGA/VGA-bold for 8x14 and 8x16.

This package contains Terminus Font for Linux console.

%description console -l pl
Font Terminus jest zaprojektowany do d�ugiej (8 i wi�cej godzin
dziennie) pracy z komputerami. Wersja 4.09 zawiera 594 znaki,
pokrywaj�ce strony kodowe ISO8859-1/2/5/9/13/15/16,
Windows-1250/1251/1252/1254/1257, IBM-437/852/855/866, KOI8-R/U/E/F,
Bulgarian-MIK,Paratype-PT154/PT254, Macintosh-Ukrainian i Esperanto, a
tak�e znaki pseudograficzne vt100 i xterma.

Dost�pne s� rozmiary 8x14, 8x16, 10x20, 12x24, 14x28 i 16x32. Style to
normalny i pogrubiony, oraz pogrubiony EGA/VGA dla 8x14 i 8x16.

Ten pakiet zawiera font Terminus dla konsoli Linuksa.

%package X11
Summary:	A clean fixed width font
Summary(pl):	Przejrzysty font o sta�ej szeroko�ci
Group:		Fonts

%description X11
Terminus Font is designed for long (8 and more hours per day) work
with computers. Version 4.09 contains 594 characters, covering code
pages ISO8859-1/2/5/9/13/15/16, Windows-1250/1251/1252/1254/1257,
IBM-437/852/855/866, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian and Esperanto, and also the
vt100 and xterm pseudographic characters.

The sizes present are 8x14, 8x16, 10x20, 12x24, 14x28 and 16x32. The
styles are normal and bold, plus EGA/VGA-bold for 8x14 and 8x16.

This package contains Terminus Font for X11 displays.

%description X11 -l pl
Font Terminus jest zaprojektowany do d�ugiej (8 i wi�cej godzin
dziennie) pracy z komputerami. Wersja 4.09 zawiera 594 znaki,
pokrywaj�ce strony kodowe ISO8859-1/2/5/9/13/15/16,
Windows-1250/1251/1252/1254/1257, IBM-437/852/855/866, KOI8-R/U/E/F,
Bulgarian-MIK,Paratype-PT154/PT254, Macintosh-Ukrainian i Esperanto, a
tak�e znaki pseudograficzne vt100 i xterma.

Dost�pne s� rozmiary 8x14, 8x16, 10x20, 12x24, 14x28 i 16x32. Style to
normalny i pogrubiony, oraz pogrubiony EGA/VGA dla 8x14 i 8x16.

Ten pakiet zawiera font Terminus dla X11.

%prep
%setup -q

%build
%{__make}

%install

%{__make} install \
	x11dir=$RPM_BUILD_ROOT/usr/share/fonts/local \
	psfdir=$RPM_BUILD_ROOT/lib/kbd/consolefonts
	
%clean
rm -rf $RPM_BUILD_ROOT

%post X11
fontpostinst local

%postun X11
fontpostinst local

%files console
%defattr(644,root,root,755)
%doc README
/lib/kbd/consolefonts/*

%files X11
%defattr(644,root,root,755)
%doc README
/usr/share/fonts/local/*
