#
# Conditional build:
%bcond_with	obsolete_sip4	# whether to obsolete sip 4 (not a replacement)

Summary:	SIP - Python/C++ Bindings Generator
Summary(pl.UTF-8):	SIP - generator wiązań Python/C++
Name:		sip6
Version:	6.14.0
Release:	1
License:	GPL v2
#Source0Download: https://pypi.org/project/sip/
Source0:	https://files.pythonhosted.org/packages/source/s/sip/sip-%{version}.tar.gz
# Source0-md5:	aae7959f6600739d3ad0a879c6541e93
URL:		https://www.riverbankcomputing.com/software/sip
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.9
BuildRequires:	python3-installer
BuildRequires:	python3-setuptools >= 1:64
BuildRequires:	python3-setuptools_scm >= 8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{_ver_lt "%{py3_ver}" "3.11"}
Requires:	python3-tomli
%endif
%if %{with obsolete_sip4}
Obsoletes:	python-sip < 2:6
Obsoletes:	python-sip-devel < 2:6
Obsoletes:	python3-sip < 2:6
Obsoletes:	python3-sip-devel < 2:6
Obsoletes:	sip < 2:6
%endif
Obsoletes:	sip5 < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be
used to create bindings for any C or C++ library. For example it is
also used to generate wxPython, the Python bindings for wxWidgets.

%description -l pl.UTF-8
SIP to zbiór narzędzi ułatwiających tworzenie wiązań Pythona do
bibliotek C i C++. Pierwotnie powstał w 1998 roku, aby stworzyć PyQt -
wiązań Pythona do biblioteki Qt, ale może być używany do tworzenia
wiązań do dowolnej biblioteki C lub C++. Jest używana także np. do
generowania wxPythona - wiązań Pythona do wxWidgets.

%prep
%setup -q -n sip-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/sip-build
%attr(755,root,root) %{_bindir}/sip-distinfo
%attr(755,root,root) %{_bindir}/sip-install
%attr(755,root,root) %{_bindir}/sip-module
%attr(755,root,root) %{_bindir}/sip-sdist
%attr(755,root,root) %{_bindir}/sip-wheel
%{py3_sitescriptdir}/sip-%{version}.dist-info
%dir %{py3_sitescriptdir}/sipbuild
%{py3_sitescriptdir}/sipbuild/*.py
%{py3_sitescriptdir}/sipbuild/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/distinfo
%{py3_sitescriptdir}/sipbuild/distinfo/*.py
%{py3_sitescriptdir}/sipbuild/distinfo/__pycache__
%{py3_sitescriptdir}/sipbuild/generator/*.py
%dir %{py3_sitescriptdir}/sipbuild/generator
%{py3_sitescriptdir}/sipbuild/generator/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/generator/outputs
%{py3_sitescriptdir}/sipbuild/generator/outputs/*.py
%{py3_sitescriptdir}/sipbuild/generator/outputs/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/generator/outputs/code
%{py3_sitescriptdir}/sipbuild/generator/outputs/code/*.py
%{py3_sitescriptdir}/sipbuild/generator/outputs/code/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/generator/outputs/formatters
%{py3_sitescriptdir}/sipbuild/generator/outputs/formatters/*.py
%{py3_sitescriptdir}/sipbuild/generator/outputs/formatters/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/generator/parser
%{py3_sitescriptdir}/sipbuild/generator/parser/*.py
%{py3_sitescriptdir}/sipbuild/generator/parser/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/generator/parser/ply
%{py3_sitescriptdir}/sipbuild/generator/parser/ply/*.py
%{py3_sitescriptdir}/sipbuild/generator/parser/ply/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/generator/resolver
%{py3_sitescriptdir}/sipbuild/generator/resolver/*.py
%{py3_sitescriptdir}/sipbuild/generator/resolver/__pycache__
%dir %{py3_sitescriptdir}/sipbuild/module
%{py3_sitescriptdir}/sipbuild/module/*.py
%{py3_sitescriptdir}/sipbuild/module/__pycache__
%{py3_sitescriptdir}/sipbuild/module/source
%dir %{py3_sitescriptdir}/sipbuild/tools
%{py3_sitescriptdir}/sipbuild/tools/*.py
%{py3_sitescriptdir}/sipbuild/tools/__pycache__
