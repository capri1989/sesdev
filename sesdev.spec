#
# spec file for package sesdev
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?el8} || (0%{?fedora} && 0%{?fedora} < 30)
%{python_enable_dependency_generator}
%endif

Name:           sesdev
Version:        1.0.3
Release:        1%{?dist}
Summary:        CLI tool to deploy and manage SES clusters
License:        MIT
%if 0%{?suse_version}
Group:          Development/Languages/Python
%endif
URL:            https://github.com/rjfd/sesdev
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?suse_version}
BuildRequires:  python-rpm-macros
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  fdupes
BuildRequires:  python3-setuptools

%if 0%{?suse_version}
Requires:       python3-click >= 6.7
Requires:       python3-Jinja2 >= 2.10.1
Requires:       python3-pycryptodomex >= 3.4.6
Requires:       python3-PyYAML >= 3.13
Requires:       python3-setuptools
%endif
Requires:       vagrant
Requires:       vagrant-libvirt

%description
sesdev is a CLI tool for developers to help with deploying SES clusters.
This tool uses vagrant and libvirt to create VMs and install Ceph using
DeepSea. The tool is highly customizable and allows to choose different
versions of Ceph and SES, as well as, different versions of the openSUSE
based OS.

%prep
%autosetup -n sesdev-%{version} -p1
%if 0%{?fedora} < 30
sed -i -e 's/^\s*lv.qemu_use_session = false$//g' seslib/templates/Vagrantfile.j2
%endif

%build
%py3_build

%install
%py3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{python3_sitelib}/ses*
%{_bindir}/sesdev

%changelog

