Summary:	Command Line Progress Bar
Summary(pl.UTF-8):	Pasek postępu w linii komend
Name:		bar
Version:	1.10.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/clpbar/%{name}_%{version}.tar.gz
# Source0-md5:	d824415b391a3f826b410c86223e54a5
URL:		http://clpbar.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bar is a simple tool to copy a stream of data and print a display for
the user on stderr showing (a) the amount of data passed, (b) the
throughput of the data transfer, and (c) the transfer time, or, if the
total size of the data stream is known, the estimated time remaining,
what percentage of the data transfer has been completed, and a
progress bar.

Bar was originally written for the purpose of estimating the amount of
time needed to transfer large amounts (many, many gigabytes) of data
across a network. (Usually in an SSH/tar pipe.)

%description -l pl.UTF-8
Bar jest prostym narzędziem kopiującym strumienie danych
i wyświetlającym użytkownikowi (a) ile danych zostało przesłanych,
(b) przepustowość przesyłu danych, (c) czas przesyłu lub, gdy znany
jest rozmiar strumienia danych, oszacowany pozostały czas, procent
ukończenia i pasek postępu.

Bar początkowo został napisany w celu oszacowania czasu potrzebnego
na przesył dużej ilości danych (wiele, wiele gigabajtów) przez sieć.
(Na przykład przez rurkę SSH/tar).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO TROUBLESHOOTING
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/bar.1*
