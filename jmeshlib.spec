%global origname JMeshLib

Name:           jmeshlib
Version:        1.2
Release:        1%{?dist}
Summary:        C++ API to work with manifold triangle meshes

License:        GPLv2+
URL:            http://jmeshlib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{origname}-%{version}.zip
Patch0:         libjmesh-compile-fixes.patch
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  gcc-c++

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -n %{origname}-%{version} -S git

%if 0%{?__isa_bits} == 64
%global optflags %(echo %{optflags} -DIS64BITPLATFORM)
%endif

mv include/clustergraph.h include/clusterGraph.h
rm -rf lib/*

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_includedir}/%{name}
install -p -m0755 src/libjmesh.so.0 %{buildroot}%{_libdir}
ln -s libjmesh.so.0 %{buildroot}%{_libdir}/libjmesh.so
install -p -m0644 include/*.h %{buildroot}%{_includedir}/%{name}
install -p -m0755 test/test %{buildroot}%{_bindir}/meshfix

%files
%license gpl.txt
%{_bindir}/meshfix
%{_libdir}/libjmesh.so.0

%files devel
%{_includedir}/%{name}/
%{_libdir}/libjmesh.so

%changelog
* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.2-1
- Initial package
