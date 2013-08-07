from ecell4.reaction_reader.decorator2 import species_attributes, reaction_rules
from ecell4.reaction_reader.species import generate_reactions

@species_attributes
def attributegen():
    R(l,l) | Rec_tot
    L(r,r,r) | Lig_tot

@reaction_rules
def rulegen():
    R(l) + L(r,r,r)     == R(l^1).L(r^1,r,r)      | (kp1, koff)
    R(l) + L(r,r,r^_)   == R(l^1).L(r^1,r,r^_)    | (kp2, koff)
    R(l) + L(r,r^_1,r^_2) == R(l^1).L(r^1,r^_1,r^_2) | (kp2, koff)

if __name__ == "__main__":
    newseeds = []
    for i, (sp, attr) in enumerate(attributegen()):
        print i, sp, attr
        newseeds.append(sp)
    print ''

    rules = rulegen()
    for i, rr in enumerate(rules):
        print i, rr
    print ''

    generate_reactions(newseeds, rules)


## Trivalent-ligand, Bivalen-receptor model
## (requires NFsim installation!)
##
## References:
## 1) B Goldstein, AS Perelson. "Equilibrium theory for the clustering
##      of bivalent cell surface receptors by trivalent ligands".
##      Biophysical Journal. 1985, vol45, p1109-1123. 
## 2) MW Sneddon, JR Faeder, T Emonet. "Efficient modeling, simulation and
##      course-graining of biological complexity with NFsim".
##      Nature methods. 2011, vol8, p177-183.
#begin model
#begin parameters
#    ## Sol-gel Phase
#    Lig_tot  4200
#    Rec_tot  300
#    cTot     0.84
#    beta     50
#    koff     0.01
#    
#    kp1 (cTot*koff)/(3.0*Lig_tot)  #FREE BINDING RATE
#    kp2 (beta*koff)/Rec_tot        #CROSSLINKING RATE
#end parameters
#begin molecule types
#    R(l,l)
#    L(r,r,r)
#end molecule types
#begin seed species
#    R(l,l)     Rec_tot
#    L(r,r,r)   Lig_tot
#end seed species
#begin observables
#    Species    Clusters  R(l!0).L(r!0,r!1).R(l!1)  # Any species with crosslinked receptors
#    Molecules  LRmotif   L(r!0).R(l!0)
#    Molecules  Lfreesite L(r)
#    Molecules  Rfreesite R(l)
#    Species    Lmonomer  L(r,r,r)
#    Species    Rmonomer  R(l,l)
#    Molecules  Ltot      L()    
#    Molecules  Rtot      R() 
#end observables
#begin reaction rules
#    R(l) + L(r,r,r)     <-> R(l!1).L(r!1,r,r)      kp1, koff
#    R(l) + L(r,r,r!+)   <-> R(l!1).L(r!1,r,r!+)    kp2, koff
#    R(l) + L(r,r!+,r!+) <-> R(l!1).L(r!1,r!+,r!+)  kp2, koff
#end reaction rules
#end model
#
### actions ##
#simulate_nf({t_start=>0,t_end=>200,n_steps=>200,complex=>1})
