Grabbing NIST Physics Data
==========================

This is a simple Python API for grabbing free tabulated NIST physics data. The target forms with POST data which map to Python properties are described in a YAML. Currently only the elemental photon cross section data is supported, however it is easy to add a schema for other datasets.

    from nist import PhotonCrossSection
    cross_section = PhotonCrossSection(atomic_number=80)
  
Data available includes:

    cross_section.CoherentScattering
    cross_section.Edge
    cross_section.IncoherentScattering
    cross_section.PairProductionInElectronField
    cross_section.PairProductionInNuclearField
    cross_section.PhotoElectricAbsorption
    cross_section.PhotonEnergy
    cross_section.TotalAttenuationWithCoherentScattering
    cross_section.TotalAttenuationWithoutCoherentScattering

Installation
------------
    git clone https://github.com/christopherpoole/pynist.git
    cd pynist/
    sudo python setup.py install

