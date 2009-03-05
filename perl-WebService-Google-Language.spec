#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WebService
%define	pnam	Google-Language
Summary:	WebService::Google::Language - Perl interface to the Google AJAX Language API
Name:		perl-WebService-Google-Language
Version:	0.09
Release:	0.11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WebService/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7b9cc05a8bf9601fafccc6a6735d6589
URL:		http://search.cpan.org/dist/WebService-Google-Language/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-JSON >= 2
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebService::Google::Language is an object-oriented interface to the
Google AJAX Language API <http://code.google.com/apis/ajaxlanguage/>.

The AJAX Language API is a web service to translate and detect the
language of blocks of text.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# XXX dir
%dir %{perl_vendorlib}/WebService/Google
%{perl_vendorlib}/WebService/Google/*.pm
%{_mandir}/man3/*
