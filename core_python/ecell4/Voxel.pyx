from cython.operator cimport dereference as deref
from cython cimport address


cdef class Voxel:

    def __cinit__(self, ParticleID pid, Species sp):
        self.thisptr = new Cpp_Voxel()
        self.thisptr.id = deref(pid.thisptr)
        self.thisptr.species = deref(sp.thisptr)

    def __dealloc__(self):
        del self.thisptr

    property id:
        def __get__(self):
            return ParticleID_from_Cpp_ParticleID(address(self.thisptr.id))

    property species:
        def __get__(self):
            return Species_from_Cpp_Species(address(self.thisptr.species))

cdef Voxel Voxel_from_Cpp_Voxel(Cpp_Voxel* v):
    cdef Cpp_Voxel *new_obj = new Cpp_Voxel(<Cpp_Voxel> deref(v))
    r = Voxel(ParticleID(0, 0), Species(""))
    del r.thisptr
    r.thisptr = new_obj
    return r
