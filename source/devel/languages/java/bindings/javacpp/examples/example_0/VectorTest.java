
/*
To demonstrate its relative ease of use even in the face of complex data types,
* imagine we had a C++ function that took a `vector<vector<void*> >` as argument.
* To get the job done with JavaCPP, we could easily define a bare-bones class
* such as this one (although having an IDE generate that code for us would be
* even better):
*/


import com.googlecode.javacpp.*;
import com.googlecode.javacpp.annotation.*;

@Platform(include="<vector>")
public class VectorTest {

    @Name("std::vector<std::vector<void*> >") @Index
    public static class PointerVectorVector extends Pointer {
        static { Loader.load(); }
        public PointerVectorVector()       { allocate();  }
        public PointerVectorVector(long n) { allocate(n); }
        public PointerVectorVector(Pointer p) { super(p); } // this = (vector<vector<void*> >*)p
        private native void allocate();                  // this = new vector<vector<void*> >()
        private native void allocate(long n);            // this = new vector<vector<void*> >(n)
        @Name("operator=")
        public native @ByRef PointerVectorVector copy(@ByRef PointerVectorVector x);

        @Name("operator[]")
        public native @Adapter("VectorAdapter<void*>") PointerPointer get(long n);
        public native @Adapter("VectorAdapter<void*>") PointerPointer at(long n);

        public native long size();
        public native @Cast("bool") boolean empty();
        public native void resize(long n);
        public native @Index(1) long size(long i);
        public native @Index(1) @Cast("bool") boolean empty(long i);
        public native @Index(1) void resize(long i, long n);

        // These two depend on the class-level @Index annotation.
        public native Pointer get(long i, long j);         // return this[i][j]
        public native void put(long i, long j, Pointer p); // this[i][j] = p
    }

    public static void main(String[] args) {
        PointerVectorVector v = new PointerVectorVector(13);
        v.resize(0, 42); // v[0].resize(42)
        Pointer p = new Pointer() { { address = 0xDEADBEEFL; } };
        v.put(0, 0, p);  // v[0][0] = p

        PointerVectorVector v2 = new PointerVectorVector().copy(v);
        Pointer p2 = v2.get(0).get(); // p2 = *(&v[0][0])
        System.out.println(v2.size() + " " + v2.size(0) + "  " + p2);

        v2.at(42);
    }
}
