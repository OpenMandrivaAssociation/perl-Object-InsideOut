%define module	Object-InsideOut
%define name	perl-%{module}
%define version 3.17
%define rel     1

Name:		    %{name}
Version:	    %{version}
Release:	    %mkrel 1
Summary:	    Comprehensive inside-out object support perl module
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}/
Source:		    http://www.cpan.org/modules/by-module/Object/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(attributes)
BuildRequires:	perl(Exception::Class)
BuildArch:	    noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}
# optional, and lead to a requires loop
%define _requires_exceptions perl\(Math::Random::MT::Auto)\  

%description
This module provides comprehensive support for implementing classes using the
inside-out object model.

Using inside-out object model, objects are not a blessed hash reference, but
merely a blessed scalar. The foobar attribute, instead of being accessed via
$self->{foobar}, is accessed using a package lexical variable @foobar (common
for every object of the class) via $foobar[$$self]. 

Advantages of this OO scheme are:
1 - speed
2 - encapsulation
3 - compilation-time checks

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/Bundle/Object/InsideOut.pm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Object
%{_mandir}/man3/*


