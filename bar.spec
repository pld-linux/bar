Summary:	Command Line Progress Bar
Summary(pl):	Pasek postêpu w linii komend
Name:		bar
Version:	1.10.7
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/clpbar/%{name}_%{version}.tar.gz
# Source0-md5:	3405f75b90ee72742cd75d18e7f59d09
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

%description -l pl
Bar jest prostym narzêdziem kopiuj±cym strumienie danych
i wy¶wietlaj±cym u¿ytkownikowi (a) ile danych zosta³o przes³anych,
(b) przepustowo¶æ przesy³u danych, (c) czas przesy³u lub, gdy znany
jest rozmiar strumienia danych, oszacowany pozosta³y czas, procent
ukoñczenia i pasek postêpu.

Bar pocz±tkowo zosta³ napisany w celu oszacowania czasu potrzebnego
na przesy³ du¿ej ilo¶ci danych (wiele, wiele gigabajtów) przez sieæ.
(Na przyk³ad przez rurkê SSH/tar).

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
%doc AUTHORS TODO TROUBLESHOOTING
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/bar.1*
