# kombajn-repo
A versatile mono-repo combining everything I've done, engineered to harvest knowledge across domains.


## Top-Level Structure

Each "sub-repo" has it's own readme file with documentation.

- **DevOps/**  
  Contains automation scripts, infrastructure-as-code, and utilities for development and deployment.
  - **Automation/**  
    - **AnsibleHome/**: Ansible roles for configuring Raspberry Pi machines.
    - **GHA-Monitor/**: GitHub Actions monitoring agent and related code.
    - **pc-utils/**: Cross-platform development utilities and scripts.
  - **Cloud/** 
    - **AWS/**  
      - **AwsCertGenerator/**: Tools for automating TLS certificate generation and AWS deployment.
    - **Cloud-infrastructure/**: Terraform scripts for public cloud providers.

- **Embedded/**  
  Microcontroller projects and modules.
  - **MCUs/**  
    - **adcModule/**: Analog-to-digital converter module code.
    - **thermometer/**: Weather station firmware and documentation.

- **py\<project-name\>/**  
  Python-based tools and applications.
  - **pyDrive/**: Command-line tool for Google Drive management.
  - **pyWeather/**: Flask-based weather station API for Raspberry Pi.

- **RaspberryPi/**  
  Projects and resources for Raspberry Pi.
  - **retro-pi/**: Retro computing project, including hardware designs, display scripts, and setup instructions.

## Additional Files

- **LICENSE**: Repository-wide license (MIT).
- **README.md**: High-level overview and organization.