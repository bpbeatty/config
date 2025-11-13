FROM registry.fedoraproject.org/fedora:latest@sha256:471bf04b1c6d37f97d476493bdd8d84b2391696c81e915a2d913bb5a6d143504 as builder

RUN dnf install --disablerepo='*' --enablerepo='fedora,updates' --setopt install_weak_deps=0 --nodocs --assumeyes rpm-build systemd-rpm-macros wget jq git

ADD files/etc/containers /tmp/bpbeatty/signing/etc/containers
ADD files/usr/etc/containers /tmp/bpbeatty/signing/usr/etc/containers
ADD files/etc/pki /tmp/bpbeatty/signing/etc/pki

RUN mkdir -p /tmp/bpbeatty/rpmbuild/SOURCES; \
    tar cf /tmp/bpbeatty/rpmbuild/SOURCES/bpbeatty-signing.tar.gz -C /tmp bpbeatty/signing

ADD rpmspec/bpbeatty-*.spec /tmp/bpbeatty

RUN rpmbuild -ba \
    --define '_topdir /tmp/bpbeatty/rpmbuild' \
    --define '%_tmppath %{_topdir}/tmp' \
    /tmp/bpbeatty/*.spec

RUN mkdir -p /tmp/bpbeatty/{files,rpms}

# Dump a file list for each RPM for easier consumption
RUN \
    for RPM in /tmp/bpbeatty/rpmbuild/RPMS/*/*.rpm; do \
        NAME="$(rpm -q $RPM --queryformat='%{NAME}')"; \
        mkdir "/tmp/bpbeatty/files/${NAME}"; \
        rpm2cpio "${RPM}" | cpio -idmv --directory "/tmp/bpbeatty/files/${NAME}"; \
        cp "${RPM}" "/tmp/bpbeatty/rpms/$(rpm -q "${RPM}" --queryformat='%{NAME}.%{ARCH}.rpm')"; \
    done

FROM scratch

# Copy build RPMs
COPY --from=builder /tmp/bpbeatty/rpms /rpms
# Copy dumped RPM content
COPY --from=builder /tmp/bpbeatty/files /files
