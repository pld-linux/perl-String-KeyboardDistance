#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	KeyboardDistance
Summary:	String::KeyboardDistance - String Comparison Algorithm
#Summary(pl):	
Name:		perl-String-KeyboardDistance
Version:	1.01
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implmements a version of keyboard distance for fuzzy string
matching.  Keyboard distance is a measure of the physical distance between
two keys on a keyboard.  For example, 'g' has a distance of 1 from the
keys 'r', 't', 'y', 'f', 'h', 'v', 'b', and 'n'.  Immediate diagonals
(like ''r, 'y', 'v', and 'n') are considered to have a distance of 1
instead of 1.414 to help to prevent horizontal/vertical bias.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
