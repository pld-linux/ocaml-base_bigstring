#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	String type based on Bigarray, for use in I/O and C-bindings
Summary(pl.UTF-8):	Typ łańcuchowy oparty na BigArray, przeznaczony do we/wy i wiązań C
Name:		ocaml-base_bigstring
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/base_bigstring/tags
Source0:	https://github.com/janestreet/base_bigstring/archive/v%{version}/base_bigstring-%{version}.tar.gz
# Source0-md5:	cc5baac49c626ca1a6424421d66da74a
URL:		https://github.com/janestreet/base_bigstring
BuildRequires:	ocaml >= 1:4.07.0
BuildRequires:	ocaml-base-devel >= 0.14.2-2
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String type based on Bigarray, for use in I/O and C-bindings.

This package contains files needed to run bytecode executables using
base_bigstring library.

%description -l pl.UTF-8
Typ łańcuchowy oparty na BigArray, przeznaczony do we/wy i wiązań C.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki base_bigstring.

%package devel
Summary:	String type based on Bigarray, for use in I/O and C-bindings - development part
Summary(pl.UTF-8):	Typ łańcuchowy oparty na BigArray, przeznaczony do we/wy i wiązań C - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14.2-2
Requires:	ocaml-ppx_jane-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
base_bigstring library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki base_bigstring.

%prep
%setup -q -n base_bigstring-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/base_bigstring/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/base_bigstring

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%dir %{_libdir}/ocaml/base_bigstring
%{_libdir}/ocaml/base_bigstring/META
%{_libdir}/ocaml/base_bigstring/runtime.js
%{_libdir}/ocaml/base_bigstring/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/base_bigstring/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllbase_bigstring_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/base_bigstring/libbase_bigstring_stubs.a
%{_libdir}/ocaml/base_bigstring/*.cmi
%{_libdir}/ocaml/base_bigstring/*.cmt
%{_libdir}/ocaml/base_bigstring/*.cmti
%{_libdir}/ocaml/base_bigstring/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/base_bigstring/base_bigstring.a
%{_libdir}/ocaml/base_bigstring/*.cmx
%{_libdir}/ocaml/base_bigstring/*.cmxa
%endif
%{_libdir}/ocaml/base_bigstring/dune-package
%{_libdir}/ocaml/base_bigstring/opam
