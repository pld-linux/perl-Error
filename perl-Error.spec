%include	/usr/lib/rpm/macros.perl
Summary:	Error perl module
Summary(pl):	Modu³ perla Error
Name:		perl-Error
Version:	0.15
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Error/Error-%{version}.tar.gz
# Source0-md5:	81b4847fb893f18a4e85186bca5f4380
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Error perl - Error/exception handling in an OO-ish way.

%description -l pl
Modu³ perla Error - obiektowa obs³uga b³êdów/wyj±tków.

%prep
%setup -q -n Error-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Error.pm
%{_mandir}/man3/*
