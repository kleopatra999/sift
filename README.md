# Overview

This is the base package for the SANS Investigative Forensics Toolkit workstation.

This is designed to be a debian package that will place any and all SANS resources needed for the SIFT workstation and then leverage the various hook scripts to configure the system to be a SIFT workstation.

Within the debian/control file will be defined all required dependencies, and each release of the SIFT package will have all dependencies pinned to a version to promote consistency across the board in terms of user experience.