#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	KeyboardDistance
Summary:	String::KeyboardDistance - string comparison algorithm
Summary(pl):	String::KeyboardDistance - algorytm porównywania ³añcuchów
Name:		perl-String-KeyboardDistance
Version:	1.01
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	366c4b5641725eb833cca800ee85e352
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implemements a version of keyboard distance for fuzzy
string matching. Keyboard distance is a measure of the physical
distance between two keys on a keyboard. For example, 'g' has a
distance of 1 from the keys 'r', 't', 'y', 'f', 'h', 'v', 'b', and
'n'. Immediate diagonals (like 'r', 'y', 'v', and 'n') are considered
to have a distance of 1 instead of 1.414 to help to prevent
horizontal/vertical bias.

%description -l pl
Ten modu³ jest implementacj± pewnej wersji odleg³o¶ci klawiaturowej
do rozmytego dopasowywania ³añcuchów. Odleg³o¶æ klawiaturowa to miara
fizycznej odleg³o¶ci pomiêdzy dwoma klawiszami na klawiaturze. Na
przyk³ad, 'g' ma odleg³o¶æ 1 od klawiszy 'r', 't', 'y', 'f', 'h', 'v',
'b' i 'n'. Dla bezpo¶rednich s±siadów po przek±tnej (jak 'r', 'y', 'v'
i 'n') uznaje siê odleg³o¶æ 1 zamiast 1.414, aby zapobiec sk³onno¶ciom
poziomym i pionowym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
