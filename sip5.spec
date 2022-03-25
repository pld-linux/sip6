Summary:	SIP - Python/C++ Bindings Generator
Name:		sip5
Version:	5.5.0
Release:	3
License:	GPL v2
#Source0Download:        https://pypi.org/project/sip/
Source0:	https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
# Source0-md5:	657c52aff0a180fc0f481e210bc9a2ba
URL:		https://www.riverbankcomputing.com/software/sip
Patch0:		python3.10.patch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be
used to create bindings for any C or C++ library. For example it is
also used to generate wxPython, the Python bindings for wxWidgets.

%prep
%setup -q -n sip-%{version}
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/sip*
%dir %{py3_sitedir}/sipbuild
%{py3_sitedir}/sip-%{version}-py*.egg-info
%{py3_sitedir}/sipbuild/*.py
%attr(755,root,root) %{py3_sitedir}/sipbuild/*.so
%{py3_sitedir}/sipbuild/__pycache__
%dir %{py3_sitedir}/sipbuild/distinfo
%{py3_sitedir}/sipbuild/distinfo/*.py
%{py3_sitedir}/sipbuild/distinfo/__pycache__
%dir %{py3_sitedir}/sipbuild/legacy
%{py3_sitedir}/sipbuild/legacy/*.py
%{py3_sitedir}/sipbuild/legacy/__pycache__
%dir %{py3_sitedir}/sipbuild/module
%{py3_sitedir}/sipbuild/module/*.py
%{py3_sitedir}/sipbuild/module/__pycache__
%dir %{py3_sitedir}/sipbuild/tools
%{py3_sitedir}/sipbuild/tools/*.py
%{py3_sitedir}/sipbuild/tools/__pycache__
%{py3_sitedir}/sipbuild/module/source
