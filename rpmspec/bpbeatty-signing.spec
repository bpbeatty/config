Name:           bpbeatty-signing
Packager:       bpbeatty
Vendor:         bpbeatty
Version:        0.2
Release:        1%{?dist}
Summary:        Signing files and keys for Universal Blue
License:        MIT
URL:            https://github.com/bpbeatty/config

BuildArch:      noarch

Source0:        bpbeatty-signing.tar.gz

%global sub_name %{lua:t=string.gsub(rpm.expand("%{NAME}"), "^bpbeatty%-", ""); print(t)}

%description
Adds files and keys for signing Universal Blue images

%prep
%setup -q -c -T

%build
mkdir -p -m0755 %{buildroot}%{_datadir}/%{VENDOR}
mkdir -p -m0755 %{buildroot}%{_exec_prefix}/etc/containers/registries.d
mkdir -p -m0755 %{buildroot}%{_exec_prefix}/etc/pki

tar xf %{SOURCE0} -C %{buildroot}%{_datadir}/%{VENDOR} --strip-components=1
tar xf %{SOURCE0} -C %{buildroot} --strip-components=2

%files
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{sub_name}
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{sub_name}/%{_exec_prefix}/etc/containers/policy.json
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{sub_name}/%{_exec_prefix}/etc/containers/registries.d/bpbeatty.yaml
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{sub_name}/%{_exec_prefix}/etc/pki/containers/bpbeatty.pub
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{sub_name}/%{_exec_prefix}/etc/containers/registries.d/quay.io-toolbx-images.yaml
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{sub_name}/%{_exec_prefix}/etc/pki/containers/quay.io-toolbx-images.pub
%attr(0644,root,root) %{_exec_prefix}/etc/containers/policy.json
%attr(0644,root,root) %{_exec_prefix}/etc/containers/registries.d/bpbeatty.yaml
%attr(0644,root,root) %{_exec_prefix}/etc/pki/containers/bpbeatty.pub
%attr(0644,root,root) %{_exec_prefix}/etc/containers/registries.d/quay.io-toolbx-images.yaml
%attr(0644,root,root) %{_exec_prefix}/etc/pki/containers/quay.io-toolbx-images.pub

%changelog
* Sat May 18 2024 qoijjj <129108030+qoijjj@users.noreply.github.com> - 0.2
- Add signature verification for toolbx images

* Sat Jul 22 2023 Brian Beatty <brian@27megahertz.com> - 0.1
- Add package for signing files and keys
