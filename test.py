from random import randint

import numpy
import pylab

from nist import PhotonCrossSection


if __name__ == "__main__":
    cross_section = PhotonCrossSection(atomic_number=randint(1, 100))

    pylab.plot(cross_section.PhotonEnergy.data,
               cross_section.PhotoElectricAbsorption.data, 'k-')
    pylab.title("%s v. %s for %s (Z=%i)" % (cross_section.PhotonEnergy.name,
                                     cross_section.PhotoElectricAbsorption.name,
                                     cross_section.name, cross_section.atomic_number))
    pylab.xlabel("%s (%s)" % (cross_section.PhotonEnergy.name,
                              cross_section.PhotonEnergy.units))
    pylab.ylabel("%s (%s)" % (cross_section.PhotoElectricAbsorption.name,
                              cross_section.PhotoElectricAbsorption.units))

    pylab.loglog()
    pylab.grid()
    pylab.show()

