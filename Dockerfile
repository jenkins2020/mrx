FROM fedora:latest

RUN dnf -y install fedora-packager @development-tools && dnf clean all 
RUN useradd -m build && \
  usermod -a -G mock build

USER build
WORKDIR /home/build
RUN rpmdev-setuptree
