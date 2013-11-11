%define upstream_name	 Object-InsideOut
%define upstream_version 3.98

# optional, and lead to a requires loop
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Math::Random::MT::Auto\\)'
%else
%define _requires_exceptions Math::Random::MT::Auto
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Comprehensive inside-out object support perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Object/Object-InsideOut-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exception::Class)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/Bundle/Object/InsideOut.pm

%files
%doc Changes README
%{perl_vendorlib}/Object
%{_mandir}/man3/*


%changelog
* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.810.0-1mdv2011.0
+ Revision: 648092
- update to new version 3.81

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.790.0-1mdv2011.0
+ Revision: 625277
- update to new version 3.79

* Tue Nov 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.760.0-1mdv2011.0
+ Revision: 598086
- update to new version 3.76

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.750.0-1mdv2011.0
+ Revision: 596629
- update to 3.75

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.670.0-1mdv2011.0
+ Revision: 552481
- update to 3.67

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 3.640.0-1mdv2010.1
+ Revision: 518081
- update to 3.64

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 3.630.0-1mdv2010.1
+ Revision: 515365
- update to 3.63

* Thu Mar 04 2010 Jérôme Quelin <jquelin@mandriva.org> 3.620.0-1mdv2010.1
+ Revision: 514095
- update to 3.62

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 3.580.0-1mdv2010.1
+ Revision: 482078
- update to 3.58

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 3.570.0-1mdv2010.1
+ Revision: 461337
- update to 3.57

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 3.560.0-1mdv2010.0
+ Revision: 408828
- update to 3.56

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 3.550.0-1mdv2010.0
+ Revision: 406177
- rebuild using %%perl_convert_version

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.55-1mdv2010.0
+ Revision: 373773
- update to new version 3.55

* Thu Feb 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.54-1mdv2009.1
+ Revision: 342817
- update to new version 3.54

* Wed Oct 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.52-1mdv2009.1
+ Revision: 298170
- new version

* Fri Oct 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.51-1mdv2009.1
+ Revision: 296904
- update to new version 3.51

* Sat Oct 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.49-1mdv2009.1
+ Revision: 294842
- update to new version 3.49

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.48-1mdv2009.1
+ Revision: 294666
- update to new version 3.48

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.47-1mdv2009.1
+ Revision: 292321
- update to new version 3.47

* Sun Jul 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.45-1mdv2009.0
+ Revision: 234270
- update to new version 3.45

* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.43-1mdv2009.0
+ Revision: 228886
- update to new version 3.43

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.42-1mdv2009.0
+ Revision: 220147
- update to new version 3.42

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.41-1mdv2009.0
+ Revision: 208358
- update to new version 3.41

* Tue Mar 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.39-1mdv2008.1
+ Revision: 185145
- update to new version 3.39

* Wed Feb 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.38-1mdv2008.1
+ Revision: 175720
- update to new version 3.38

* Thu Feb 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.37-1mdv2008.1
+ Revision: 173548
- update to new version 3.37

* Sat Feb 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.36-1mdv2008.1
+ Revision: 169258
- update to new version 3.36

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.35-1mdv2008.1
+ Revision: 136770
- update to new version 3.35

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.34-1mdv2008.1
+ Revision: 113648
- update to new version 3.34

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.33-1mdv2008.1
+ Revision: 107979
- update to new version 3.33
- update to new version 3.32
- update to new version 3.29
- update to new version 3.28

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.27-1mdv2008.1
+ Revision: 105896
- update to new version 3.27

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.26-1mdv2008.1
+ Revision: 97534
- update to new version 3.26

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.21-1mdv2008.0
+ Revision: 69243
- update to new version 3.21

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.19-1mdv2008.0
+ Revision: 47701
- update to new version 3.19

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 3.17-1mdv2008.0
+ Revision: 29067
- Update to new version 3.17

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 3.14-1mdv2008.0
+ Revision: 20960
- update to 3.14


* Wed Mar 21 2007 Michael Scherer <misc@mandriva.org> 3.11-2mdv2007.1
+ Revision: 147544
- Fix missing deps. Math::Random::MT::Auto requires perl-Object-InsideOut

* Mon Mar 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.11-1mdv2007.1
+ Revision: 141924
- new version

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.49-1mdv2007.0
- New version 1.49

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.48-1mdv2007.0
- New version 1.48

* Sat Jul 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.45-1mdv2007.0
- New version 1.45

* Tue Jun 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.44-1mdv2007.0
- New version 1.44

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-1mdv2007.0
- New release 1.42
- spec cleanup

* Wed May 03 2006 Michael Scherer <misc@mandriva.org> 1.41-2mdk
- BuildRequires fix
- enhances description, thanks to jq

* Tue May 02 2006 Michael Scherer <misc@mandriva.org> 1.41-1mdk
- First Mandriva package, fix #22223



