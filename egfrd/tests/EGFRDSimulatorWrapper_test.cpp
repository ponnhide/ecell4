#define BOOST_TEST_MODULE "EGFRDSimulatorWrapper_test"
#define BOOST_TEST_NO_LIB

#include <boost/test/included/unit_test.hpp>

#include <ecell4/core/types.hpp>
#include <ecell4/core/Species.hpp>
#include <ecell4/core/Position3.hpp>
#include <ecell4/core/NetworkModel.hpp>

#include "../EGFRDWorld.hpp"
#include "../EGFRDSimulatorWrapper.hpp"

#include <iostream>

using namespace ecell4;
using namespace ecell4::egfrd;


BOOST_AUTO_TEST_CASE(EGFRDSimulatorWrapper_test_constructor)
{
    const Real L(1e-6);
    std::string D("1e-12"), radius("2.5e-9");

    boost::shared_ptr<NetworkModel> model(new NetworkModel());

    Species sp1("A");
    sp1.set_attribute("D", D);
    sp1.set_attribute("radius", radius);
    (*model).add_species(sp1);

    boost::shared_ptr<EGFRDWorld> world(new EGFRDWorld(L));

    (*world).add_species(sp1);

    ParticleInfo info1((*world).get_particle_info(sp1));
    ecell4::Particle const p1(
        sp1, Position3(0, 0, 0), info1.radius, info1.D);
    ecell4::ParticleID const pid1((*world).new_particle(p1));
    ecell4::Particle const p2(
        sp1, Position3(6e-9, 0, 0), info1.radius, info1.D);
    ecell4::ParticleID const pid2((*world).new_particle(p2));

    std::cout << (*world).num_particles() << std::endl;
    std::cout << (*world).num_particles(sp1) << std::endl;
    std::cout << (*world).get_particle(pid1).second.position() << std::endl;

    EGFRDSimulatorWrapper sim(model, world);

    for (int i(0); i < 10000; ++i)
    {
        std::cout << "t=" << sim.t() << std::endl;
        sim.step();
    }

    // BOOST_ASSERT(false);
}
