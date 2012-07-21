Summary:	A clean fixed width font
Summary(pl.UTF-8):	Przejrzysty font o stałej szerokości
Name:		terminus-font
Version:	4.38
Release:	1
Epoch:		0
License:	SIL Open Font License v1.1 (font), GPL v2+ (utils)
Group:		Fonts
Source0:	http://downloads.sourceforge.net/terminus-font/%{name}-%{version}.tar.gz
# Source0-md5:	a8e792fe6e84c86ed2b6ed3e2a12ba66
URL:		http://sourceforge.net/projects/terminus-font/
BuildRequires:	perl-base
BuildRequires:	xorg-app-bdftopcf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminus Font is designed for long (8 and more hours per day) work
with computers. Now it contains 856 characters and covers 120 language
sets and the following code pages: ISO8859-1/2/5/7/9/13/15/16,
IBM-437/852/855/866, Windows-1250/1251/1252/1254/1257, KOI8-R/U/E/F,
Bulgarian-MIK, Paratype-PT154/PT254, Macintosh-Ukrainian and
Esperanto, and also the vt100 and xterm pseudographic characters.

The sizes present are 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,
14x28 and 16x32. The styles are normal and bold, plus EGA/VGA-bold for
8x14 and 8x16.

%description -l pl.UTF-8
Font Terminus jest zaprojektowany do długiej (8 i więcej godzin
dziennie) pracy z komputerami. Obecna wersja zawiera 856 znaków,
pokrywających 120 języków i następujące strony kodowe:
ISO8859-1/2/5/7/9/13/15/16, IBM-437/852/855/866,
Windows-1250/1251/1252/1254/1257, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian i Esperanto, a także znaki
pseudograficzne vt100 i xterma.

Dostępne są rozmiary 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,
14x28 i 16x32. Style to normalny i pogrubiony, oraz pogrubiony EGA/VGA
dla 8x14 i 8x16.

%package console
Summary:	A clean fixed width font
Summary(pl.UTF-8):	Przejrzysty font o stałej szerokości
License:	SIL Open Font License v1.1
Group:		Fonts

%description console
Terminus Font is designed for long (8 and more hours per day) work
with computers. Now it contains 856 characters and covers 120 language
sets and the following code pages: ISO8859-1/2/5/7/9/13/15/16,
IBM-437/852/855/866, Windows-1250/1251/1252/1254/1257, KOI8-R/U/E/F,
Bulgarian-MIK, Paratype-PT154/PT254, Macintosh-Ukrainian and
Esperanto, and also the vt100 and xterm pseudographic characters.

The sizes present are 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,
14x28 and 16x32. The styles are normal and bold, plus EGA/VGA-bold for
8x14 and 8x16.

This package contains Terminus Font for Linux console.

%description console -l pl.UTF-8
Font Terminus jest zaprojektowany do długiej (8 i więcej godzin
dziennie) pracy z komputerami. Obecna wersja zawiera 856 znaków,
pokrywających 120 języków i następujące strony kodowe:
ISO8859-1/2/5/7/9/13/15/16, IBM-437/852/855/866,
Windows-1250/1251/1252/1254/1257, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian i Esperanto, a także znaki
pseudograficzne vt100 i xterma.

Dostępne są rozmiary 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,
14x28 i 16x32. Style to normalny i pogrubiony, oraz pogrubiony EGA/VGA
dla 8x14 i 8x16.

Ten pakiet zawiera font Terminus dla konsoli Linuksa.

%package X11
Summary:	A clean fixed width font
Summary(pl.UTF-8):	Przejrzysty font o stałej szerokości
License:	SIL Open Font License v1.1
Group:		Fonts
Requires(post,postun):	fontpostinst

%description X11
Terminus Font is designed for long (8 and more hours per day) work
with computers. Now it contains 856 characters and covers 120 language
sets and the following code pages: ISO8859-1/2/5/7/9/13/15/16,
IBM-437/852/855/866, Windows-1250/1251/1252/1254/1257, KOI8-R/U/E/F,
Bulgarian-MIK, Paratype-PT154/PT254, Macintosh-Ukrainian and
Esperanto, and also the vt100 and xterm pseudographic characters.

The sizes present are 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,
14x28 and 16x32. The styles are normal and bold, plus EGA/VGA-bold for
8x14 and 8x16.

This package contains Terminus Font for X11 displays.

%description X11 -l pl.UTF-8
Font Terminus jest zaprojektowany do długiej (8 i więcej godzin
dziennie) pracy z komputerami. Obecna wersja zawiera 856 znaków,
pokrywających 120 języków i następujące strony kodowe:
ISO8859-1/2/5/7/9/13/15/16, IBM-437/852/855/866,
Windows-1250/1251/1252/1254/1257, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian i Esperanto, a także znaki
pseudograficzne vt100 i xterma.

Dostępne są rozmiary 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,
14x28 i 16x32. Style to normalny i pogrubiony, oraz pogrubiony EGA/VGA
dla 8x14 i 8x16.

Ten pakiet zawiera font Terminus dla X11.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	x11dir=$RPM_BUILD_ROOT%{_datadir}/fonts/local \
	psfdir=$RPM_BUILD_ROOT/lib/kbd/consolefonts

%clean
rm -rf $RPM_BUILD_ROOT

%post X11
fontpostinst local

%postun X11
fontpostinst local

%files console
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
/lib/kbd/consolefonts/ter-*.psf.gz

%files X11
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%{_datadir}/fonts/local/ter-*.pcf.gz
