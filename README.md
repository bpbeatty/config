[![build-config](https://github.com/bpbeatty/config/actions/workflows/build.yml/badge.svg)](https://github.com/bpbeatty/config/actions/workflows/build.yml)

# bpbeatty configs

A layer for adding signing configs.

# Usage

Add this to your Containerfile:

    COPY --from=ghcr.io/bpbeatty/config:latest /rpms/config/bpbeatty-signing*.rpm
    RUN rpm -ivh /bpbeatty-signing*.rpm

# Verification

These images are signed with sisgstore's [cosign](https://docs.sigstore.dev/cosign/overview/). You can verify the signature by downloading the `cosign.pub` key from this repo and running the following command:

    cosign verify --key cosign.pub ghcr.io/bpbeatty/config

