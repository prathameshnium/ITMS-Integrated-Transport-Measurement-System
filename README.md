
# Integrated Transport Measurement System (Supplementary Material)

![Project Inception](https://img.shields.io/badge/Project_Inception-June_2022-blue?style=flat-square)
![Project Age](https://img.shields.io/badge/Project_Age-3%2B_Years-success?style=flat-square)
![Status](https://img.shields.io/badge/Status-Operational-brightgreen?style=flat-square)
[![Software](https://img.shields.io/badge/Software-PICA_Suite-blue?style=flat-square)](https://github.com/prathameshnium/PICA-Python-Instrument-Control-and-Automation)
![Docs Health](https://github.com/prathameshnium/ITMS-Hardware/actions/workflows/link-check.yml/badge.svg)

The ITMS is an indigenously developed system designed for novel and advanced characterisation, implemented using a low-cost, modular experimental setup.

**Affiliation:** UGC-DAE Consortium for Scientific Research, Mumbai Centre & Savitribai Phule Pune University  
**Funding:** SERB-CRG Grant No. CRG/2022/005676  
**Facility In‑Charge:** Dr. Sudip Mukherjee, Scientist‑F

---

## 1. Overview
The measurement system has been developed entirely in-house and is hereafter referred to as the **Integrated Transport Measurement System (ITMS)**.

This repository provides a **technical description** of the ITMS, the modular cryogenic measurement platform described in the upcoming manuscript. It covers the system architecture, measurement capabilities, probe inserts, and operating ranges. A detailed user manual will be added. Design files (schematics, CAD models, BOM) are not published.

The associated software, **[Python-based Instrument Control and Automation (PICA)](https://github.com/prathameshnium/PICA-Python-Instrument-Control-and-Automation)**, is maintained in a separate repository to ensure modularity.

## 2. Facility Capabilities
The hardware consists of three distinct measurement inserts (probes) optimised for operations in **Liquid Nitrogen (77 K - 320 K)** and **Quantum Design PPMS (5 K - 380 K, 14 T)** environments.

### Measurement Modes
1.  **Ultra-Low Resistance:** 4-Wire Delta Mode using Keithley 6221/2182.
2.  **High Impedance:** Electrometry & Pyroelectric Current using Keithley 6517B.
3.  **Dielectric and Magnetodielectric Spectroscopy:** Frequency-dependent profiling using Keysight E4980A.
4.  **Pyroelectric Characterisation:** Spontaneous polarisation measurement using Keithley 6517B.

## 3. Measurement Inserts
The system uses the following measurement inserts (probes):

| Module Name | Environment | Primary Application | Status |
| :--- | :--- | :--- | :--- |
| **[Cryogenic Insert](https://github.com/prathameshnium/ITMS-Hardware/blob/main/modules/cryo_probe)** | Liquid Nitrogen | Low-Noise Transport, Pyroelectric Current | **Active** |
| **[PPMS Interface](https://github.com/prathameshnium/ITMS-Hardware/blob/main/modules/ppms_insert)** | QD PPMS | Magnetodielectric, Hall Effect | **Active** |

---

## 4. Acknowledgements
We acknowledge the financial support provided under the **SERB-CRG project grant No. CRG/2022/005676** from the **Anusandhan National Research Foundation (ANRF)**, a statutory body of the Department of Science and Technology (DST), Government of India.

## 5. Legal & Licensing

### Intellectual Property
**Copyright © 2026 UGC-DAE Consortium for Scientific Research, Mumbai Centre.**

The documentation in this repository is licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://github.com/prathameshnium/ITMS-Hardware/blob/main/LICENCE).

**Proprietary Notice:** This repository contains a **system description** only. Design files and all proprietary institutional files remain the intellectual property of **UGC-DAE CSR, Mumbai Centre**. The content is strictly limited to academic validation metrics and standard operating procedures for open research. No restricted, classified, or export-controlled technical data is hosted here.

### Disclaimer
This project is not affiliated with, endorsed by, or connected to Quantum Design Inc. "PPMS" is a trademark of Quantum Design. The ITMS PPMS Interface Module is a custom accessory designed to operate with standard equipment.

### Cite this Repository
If you refer to this system or its documentation in your research, please cite:

```bibtex
@misc{ITMS_Hardware_2026,
  author = {Deshmukh, Prathamesh and Mukherjee, Sudip},
  title = {Integrated Transport Measurement System (Supplementary Material)},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/prathameshnium/ITMS-Hardware}}
}

```
**Research Impact:** Papers that used or cite ITMS are listed in [RESEARCH_IMPACT.md](https://github.com/prathameshnium/ITMS-Hardware/blob/main/RESEARCH_IMPACT.md).

**Contact:** For technical inquiries, please create an [Issue](https://github.com/prathameshnium/ITMS-Hardware/issues) in this repository.
