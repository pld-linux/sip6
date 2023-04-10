Summary:	SIP - Python/C++ Bindings Generator
Name:		sip6
Version:	6.7.8
Release:	1
License:	GPL v2
#Source0Download:        https://pypi.org/project/sip/
Source0:	https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
# Source0-md5:	e9838b911b296f944ce5848b60f01f61
URL:		https://www.riverbankcomputing.com/software/sip
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
Obsoletes:	python-sip < 6
Obsoletes:	python-sip-devel < 6
Obsoletes:	python-PyQt5-sip < 6
Obsoletes:	python-PyQt5-sip-devel < 6
Obsoletes:	python3-sip < 6
Obsoletes:	python3-sip-devel < 6
Obsoletes:	python3-PyQt5-sip < 6
Obsoletes:	python3-PyQt5-sip-devel < 6
Obsoletes:	sip < 6
Obsoletes:	sip5 < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be
used to create bindings for any C or C++ library. For example it is
also used to generate wxPython, the Python bindings for wxWidgets.

%prep
%setup -q -n sip-%{version}

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
%{py3_sitedir}/sipbuild/generator/*.py
%dir %{py3_sitedir}/sipbuild/generator
%{py3_sitedir}/sipbuild/generator/__pycache__
%dir %{py3_sitedir}/sipbuild/generator/outputs
%{py3_sitedir}/sipbuild/generator/outputs/*.py
%{py3_sitedir}/sipbuild/generator/outputs/__pycache__
%dir %{py3_sitedir}/sipbuild/generator/outputs/formatters
%{py3_sitedir}/sipbuild/generator/outputs/formatters/*.py
%{py3_sitedir}/sipbuild/generator/outputs/formatters/__pycache__
%dir %{py3_sitedir}/sipbuild/generator/parser
%{py3_sitedir}/sipbuild/generator/parser/*.py
%{py3_sitedir}/sipbuild/generator/parser/__pycache__
%dir %{py3_sitedir}/sipbuild/generator/resolver
%{py3_sitedir}/sipbuild/generator/resolver/*.py
%{py3_sitedir}/sipbuild/generator/resolver/__pycache__
%dir %{py3_sitedir}/sipbuild/module
%{py3_sitedir}/sipbuild/module/*.py
%{py3_sitedir}/sipbuild/module/__pycache__
%dir %{py3_sitedir}/sipbuild/tools
%{py3_sitedir}/sipbuild/tools/*.py
%{py3_sitedir}/sipbuild/tools/__pycache__
%{py3_sitedir}/sipbuild/module/source
